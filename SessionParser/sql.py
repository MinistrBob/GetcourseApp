# create table settings
sql_ct_last_date = "CREATE TABLE last_date (id INTEGER, value TEXT)"

# create table sessions
# ВНИМАНИЕ: Поле visit_id не уникальное!!!
sql_ct_sessions = """
CREATE TABLE "sessions" (
	"visit_id",
	"start_of_visit",
	"ip",
	"traffic_type",
	"channel",
	"depth_of_view1",
	"visit_number",
	"visitor_id",
	"device",
	"login_page",
	"entrance_address",
	"login_referrer",
	"user",
	"order1",
	"channel_group",
	"expense_group_1",
	"expense_group_2",
	"campaign",
	"utm_medium",
	"utm_source",
	"keyword",
	"utm_content",
	"referrer_significant_domain",
	"referrer_domain",
	"referrer",
	"start_page",
	"depth_of_view2",
	"there_is_an_order_1",
	"there_is_an_order_2",
	"country",
	"region",
	"city",
	"ip2",
	"user_id",
	"user_url",
	"user_email",
	"user_telegram",
	"user_country",
	"user_city",
	"user_phone"
)"""
