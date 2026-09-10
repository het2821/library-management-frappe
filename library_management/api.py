import frappe


@frappe.whitelist()
def get_library_summary():
    total_books = frappe.db.count("Library Book")

    available_books = frappe.db.sql("""
        SELECT COALESCE(SUM(available_copies), 0)
        FROM `tabLibrary Book`
    """)[0][0]

    issued_books = frappe.db.count(
        "Book Issue",
        {
            "status": "Issued",
            "docstatus": 1
        }
    )

    total_members = frappe.db.count("Library Member")

    pending_fines = frappe.db.sql("""
        SELECT COALESCE(SUM(fine_amount), 0)
        FROM `tabBook Return`
        WHERE fine_status = 'Pending'
        AND docstatus = 1
    """)[0][0]

    return {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,
        "total_members": total_members,
        "pending_fines": pending_fines
    }

@frappe.whitelist()
def get_available_books():
    books = frappe.get_all(
        "Library Book",
        filters={
            "is_active": 1,
            "available_copies": [">", 0]
        },
        fields=[
            "name",
            "book_title",
            "author",
            "category",
            "total_copies",
            "available_copies",
            "shelf_location"
        ],
        order_by="book_title asc"
    )

    return books

@frappe.whitelist()
def get_member_issued_books(member):
    if not member:
        frappe.throw("Member is required.")

    if not frappe.db.exists("Library Member", member):
        frappe.throw("Library Member not found.")

    books = frappe.get_all(
        "Book Issue",
        filters={
            "member": member,
            "status": "Issued",
            "docstatus": 1
        },
        fields=[
            "name",
            "book",
            "issue_date",
            "due_date",
            "status"
        ],
        order_by="due_date asc"
    )

    return books

def get_permission_query_conditions(user):
    if not user:
        return ""

    if "Administrator" in frappe.get_roles(user):
        return ""

    member = frappe.db.get_value(
        "Library Member",
        {"user": user},
        "name"
    )

    if not member:
        return "1=0"

    return f"`tabLibrary Member`.`name` = {frappe.db.escape(member)}"

def get_permission_query_conditions(user):
    if not user:
        return ""

    if "Administrator" in frappe.get_roles(user):
        return ""

    member = frappe.db.get_value(
        "Library Member",
        {"user": user},
        "name"
    )

    if not member:
        return "1=0"

    return f"`tabLibrary Member`.`name` = {frappe.db.escape(member)}"

def get_book_issue_permission_query(user):
    if not user:
        return ""

    if "Administrator" in frappe.get_roles(user):
        return ""

    member = frappe.db.get_value(
        "Library Member",
        {"user": user},
        "name"
    )

    if not member:
        return "1=0"

    return f"`tabBook Issue`.`member` = {frappe.db.escape(member)}"

def get_book_return_permission_query(user):
    if not user:
        return ""

    if "Administrator" in frappe.get_roles(user):
        return ""

    member = frappe.db.get_value(
        "Library Member",
        {"user": user},
        "name"
    )

    if not member:
        return "1=0"

    return f"`tabBook Return`.`member` = {frappe.db.escape(member)}"
