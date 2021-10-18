from behave import *
from Navigation_test import *


@given('url is launched')
def step_impl(context):
    time.sleep(2)
    environment()


@when('I am on blavity page')
def step_impl(context):
    page_load()


@then('check whether page is loaded')
def step_impl(context):
    post_page_load_pop_up()


@then('check whether arrow element is present')
def step_impl(context):
    verify_presence_of_element_in_page()


@then('verify if ticker section exists')
def step_impl(context):
    verify_if_ticker_exists()


@then('verify ticker count and links')
def step_impl(context):
    verify_ticker_count_and_links()


@then('verify links from carousel works')
def step_impl(context):
    verify_if_all_carousel_entries_works()


@then('verify arrow buttons and read more link work in carousel')
def step_impl(context):
    verify_carousel_read_more_arrows()


@then('verify side bar top stories section and links')
def step_impl(context):
    verify_side_bar_top_stories()


@then('verify load more stories section and links')
def step_impl(context):
    verify_load_more_stories()


@then('verify subscribe banner section')
def step_impl(context):
    verify_subscribe_banner_section()


@then('verify lunchtable section')
def step_impl(context):
    verify_lunchtable_section()


@then('verify blavity originals section')
def step_impl(context):
    verify_blavity_originals_section()


@then('verify op ed section')
def step_impl(context):
    verify_page_op_ed_section()


@then('verify from our other sites section')
def step_impl(context):
    verify_from_our_other_sites()


@then('verify footer of blavity site')
def step_impl(context):
    verify_blavity_footer()


@then('verify whether nav bar is present and displayed')
def step_impl(context):
    verify_nav_bar_presence()


@then('verify whether all nav bar links are working')
def step_impl(context):
    verify_nav_bar_links()


@then('verify footer section is present and displayed')
def step_impl(context):
    verify_footer_presence()


@then('close the browser')
def step_impl(context):
    print("closing the browser instance")
    driver.quit()


"""""
verify_blavity_footer
close the browser
if text not in context.response:
    fail('%r not in %r' % (text, context.response))
"""""
