// Copyright (c) 2026, Het Thakkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book Issue", {
    onload(frm) {
        if (frm.is_new() && !frm.doc.issue_date) {
            frm.set_value("issue_date", frappe.datetime.get_today());
        }

        if (frm.is_new() && !frm.doc.due_date) {
            frm.set_value(
                "due_date",
                frappe.datetime.add_days(
                    frappe.datetime.get_today(),
                    7
                )
            );
        }
    },

    issue_date(frm) {
        if (frm.doc.issue_date) {
            frm.set_value(
                "due_date",
                frappe.datetime.add_days(
                    frm.doc.issue_date,
                    7
                )
            );
        }
    }
});
