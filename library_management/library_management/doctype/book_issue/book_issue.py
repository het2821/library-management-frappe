import frappe
from frappe.model.document import Document


class BookIssue(Document):

    def validate(self):
        self.validate_member()
        self.validate_book()
        self.validate_duplicate_issue()

    def validate_member(self):
        member = frappe.get_doc("Library Member", self.member)

        if member.status != "Active" or not member.is_active:
            frappe.throw(
                f"Member {member.member_name} is not active and cannot issue books."
            )

    def validate_book(self):
        book = frappe.get_doc("Library Book", self.book)

        if not book.is_active:
            frappe.throw(
                f"Book {book.book_title} is not active."
            )

        if book.available_copies <= 0:
            frappe.throw(
                f"No available copies of {book.book_title}."
            )

    def validate_duplicate_issue(self):
        existing_issue = frappe.db.exists(
            "Book Issue",
            {
                "member": self.member,
                "book": self.book,
                "status": "Issued",
                "docstatus": 1,
                "name": ["!=", self.name],
            },
        )

        if existing_issue:
            frappe.throw(
                f"This member already has this book issued in {existing_issue}."
            )

    def on_submit(self):
        book = frappe.get_doc("Library Book", self.book)

        if book.available_copies <= 0:
            frappe.throw(
                f"No available copies of {book.book_title}."
            )

        book.available_copies -= 1
        book.save()

    def on_cancel(self):
        book = frappe.get_doc("Library Book", self.book)

        book.available_copies += 1
        book.save()
