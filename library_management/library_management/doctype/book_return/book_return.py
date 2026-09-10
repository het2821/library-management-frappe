# Copyright (c) 2026, Het Thakkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, date_diff, today


class BookReturn(Document):

    def validate(self):
        self.validate_book_issue()
        self.calculate_late_days()
        self.calculate_fine()

    def validate_book_issue(self):
        issue = frappe.get_doc("Book Issue", self.book_issue)

        if issue.status == "Returned":
            frappe.throw("This book issue has already been returned.")

        if issue.member != self.member:
            frappe.throw("Selected member does not match the Book Issue.")

        if issue.book != self.book:
            frappe.throw("Selected book does not match the Book Issue.")

    def calculate_late_days(self):
        return_date = getdate(self.return_date)
        due_date = getdate(self.due_date)

        self.late_days = max(date_diff(return_date, due_date), 0)

    def calculate_fine(self):
        self.fine_amount = self.late_days * self.fine_per_day

        if self.fine_amount > 0:
            self.fine_status = "Pending"
        else:
            self.fine_status = "Not Applicable"

    def on_submit(self):
        book = frappe.get_doc("Library Book", self.book)

        book.available_copies += 1
        book.save()

        frappe.db.set_value("Book Issue",self.book_issue,"status","Returned")

    def on_cancel(self):
        book = frappe.get_doc("Library Book", self.book)

        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()

        frappe.db.set_value("Book Issue",self.book_issue,"status","Issued")
