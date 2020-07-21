# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pemiw"
app_title = "Pemiw"
app_publisher = "GreyCube Technologies"
app_description = "Show payment in words"
app_icon = "fa fa-money"
app_color = "yellow"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pemiw/css/pemiw.css"
# app_include_js = "/assets/pemiw/js/pemiw.js"

# include js, css files in header of web template
# web_include_css = "/assets/pemiw/css/pemiw.css"
# web_include_js = "/assets/pemiw/js/pemiw.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pemiw.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pemiw.install.before_install"
# after_install = "pemiw.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pemiw.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Payment Entry": {
		"validate": "pemiw.api.get_amount_in_words",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pemiw.tasks.all"
# 	],
# 	"daily": [
# 		"pemiw.tasks.daily"
# 	],
# 	"hourly": [
# 		"pemiw.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pemiw.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pemiw.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pemiw.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pemiw.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pemiw.task.get_dashboard_data"
# }

