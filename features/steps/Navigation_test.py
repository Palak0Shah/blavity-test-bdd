from home_page_test import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


def verify_nav_bar_presence():
    print("check whether nav bar is present or not")
    time.sleep(3)
    nav_bar = driver.find_element(By.XPATH, "//ul[@class='navbar-nav d-desktop-flex align-items-center']")
    print(nav_bar.text)
    if (nav_bar.text is not None) and (nav_bar.text != ""):
        print("Nav Bar is present")
        pass


def verify_nav_news_link():
    print("checking the News tab")
    news_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='News']")
    news_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("News - Blavity News"))
    print("Current Window Title for News Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_nav_opinions_link():
    print("checking the Opinion link")
    opinion_ed_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='Op-Eds']")
    opinion_ed_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Opinion - Blavity News"))
    print("Current Window Title for Opinion Eds Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_nav_lifestyle_link():
    print("checking the Lifestyle tab")
    life_style_link = driver.find_element(By.XPATH, "//a[@class='nav-link text-white'][normalize-space()='Lifestyle']")
    life_style_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Lifestyle - Blavity News"))
    print("Current Window Title for Life Style Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_nav_blavity_u_link():
    blavity_u_link = driver.find_element(By.XPATH, "//a[normalize-space()='BlavityU']")
    blavity_u_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Blavity U - Blavity News"))
    print("Current Window Title for Blavity U Link is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_submit_story():
    submit_a_story_link = driver.find_element(By.XPATH, "//a[normalize-space()='Submit a Story']")
    submit_a_story_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    print("Current Window Title for Submit a Story is : ", driver.title)
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))


def verify_sign_up_link():
    sign_up_link = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    sign_up_link.click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.url_to_be("https://join.blavity.com/"))
    print("Current window title for Sign Up is: " + driver.title)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("link for Sign Up Section is present and working as expected")


def verify_nav_search_bar():
    search_bar = driver.find_element(
        By.CSS_SELECTOR,
        "button[class='btn btn--search bg-transparent border-0 text-right text-white position-absolute']")
    search_bar.click()
    input_search = driver.find_element(By.XPATH, "//input[@type='text']")
    search_text = "culture"
    input_search.send_keys(search_text)
    search_bar.click()
    WebDriverWait(driver, 40).until(ec.url_contains(search_text))
    WebDriverWait(driver, 40).until(ec.title_is("Search - Blavity News"))
    print("Current window title for Search Page is: " + driver.title)
    print("link for Search is present and working as expected")


def verify_more_email_section():
    more_link_email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    more_link_email.send_keys("test@gmail0.com")
    more_link_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    more_link_checkbox.click()
    submit_more_email_link = driver.find_element(By.XPATH, "//button[normalize-space()='submit']")
    submit_more_email_link.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
        By.XPATH, "//p[@class='success-message text-silver']")))
    success_msg_on_click = driver.find_element(By.XPATH, "//p[@class='success-message text-silver']")
    if (success_msg_on_click.text is not None) and (success_msg_on_click.text != ""):
        print("Email section of more link is working as expected")


def verify_more_politics():
    more_politics_link = driver.find_element(By.XPATH, "//a[normalize-space()='Politics']")
    more_politics_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Politics - Blavity News"))
    print("Link for Politics under More Section is working as expected")


def verify_more_news():
    more_news_link = driver.find_element(By.XPATH, "//a[normalize-space()='News']")
    more_news_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("News - Blavity News"))
    # print("Current Window Title for Politics is : ", driver.title)
    print("Link for News under More Section is working as expected")


def verify_more_op_ed():
    more_op_ed_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Op-Eds']")
    more_op_ed_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Opinion - Blavity News"))
    # print("Current Window Title for Politics is : ", driver.title)
    print("Link for Op-Eds under More Section is working as expected")


def verify_more_write_a_story():
    more_write_a_story_link = driver.find_element(By.XPATH, "//a[normalize-space()='Write a Story']")
    more_write_a_story_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Write a Story under More Section is working as expected")


def verify_more_terms():
    more_terms_link = driver.find_element(By.XPATH, "//a[normalize-space()='Terms & Conditions']")
    more_terms_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Terms & Conditions under More Section is working as expected")


def verify_more_partner_with_us():
    more_partner_with_us_link = driver.find_element(By.XPATH, "//a[normalize-space()='Partner With Us']")
    more_partner_with_us_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Partner With Us under More Section is working as expected")


def verify_more_culture():
    more_culture_link = driver.find_element(By.XPATH, "//a[normalize-space()='Culture']")
    more_culture_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Culture - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Culture under More Section is working as expected")


def verify_more_my_account():
    more_my_account_link = driver.find_element(By.XPATH, "//a[normalize-space()='My Account']")
    more_my_account_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for My Account under More Section is working as expected")
    driver.back()


def verify_more_careers():
    more_careers_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Careers']")
    more_careers_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Careers under More Section is working as expected")


def verify_more_life_style():
    more_life_style_link = driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Lifestyle']")
    more_life_style_link.click()
    WebDriverWait(driver, 40).until(ec.title_is("Lifestyle - Blavity News"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for LifeStyle under More Section is working as expected")


def verify_more_privacy_policies():
    more_privacy_policies_link = driver.find_element(By.XPATH, "//a[normalize-space()='Privacy Policies']")
    more_privacy_policies_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Privacy Policy under More Section is working as expected")


def verify_more_shop():
    more_shop_link = driver.find_element(By.XPATH, "//a[normalize-space()='Shop']")
    more_shop_link.click()
    # switch to the new tab being opened.
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Link for Shop under More Section is working as expected")


def verify_more_social_justice():
    more_social_justice_link = driver.find_element(By.XPATH, "//a[normalize-space()='Social Justice']")
    more_social_justice_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Social Justice under More Section is working as expected")


def verify_more_mastercard():
    more_mastercard_link = driver.find_element(By.XPATH, "//a[normalize-space()='Blavity x Mastercard']")
    more_mastercard_link.click()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))
    # print("Current Window Title for Write a Story is : ", driver.title)
    print("Link for Blavity x Mastercard under More Section is working as expected")
    driver.back()
    WebDriverWait(driver, 40).until(ec.title_contains("Blavity"))


def verify_more_disclaimer_text():
    more_disclaimer_text = driver.find_element(
        By.XPATH, "//h6[contains(text(),'Blavity is a community of the most exceptional mul')]")
    if more_disclaimer_text.is_displayed():
        print("disclaimer anc copyright text is displayed under more section.")


def verify_more_instagram_link():
    more_instagram = driver.find_element(By.XPATH,
                                         "//div[@class='dropdown-content-footer d-none d-desktop-block']//a[1]")
    more_instagram.click()
    print("clicked on instagram link")
    verify_blavity_footer_instagram()


def verify_more_twitter_link():
    more_twitter = driver.find_element(By.XPATH,
                                         "//div[@class='dropdown-content-footer d-none d-desktop-block']//a[2]")
    more_twitter.click()
    print("clicked on twitter link")
    verify_blavity_footer_twitter()


def verify_more_facebook_link():
    more_facebook = driver.find_element\
        (By.XPATH, "//ul[@class='navbar-nav d-desktop-flex align-items-center']//a[3]")
    more_facebook.click()
    print("clicked on facebook link")
    verify_blavity_footer_facebook()


def verify_more_blavity_image():
    more_blavity_image = driver.find_element\
        (By.XPATH, "//div[@class='d-flex justify-content-end text-white']//img[@title='Blavity']")
    if more_blavity_image.is_displayed():
        print("under more section image of blavity is displayed.")

def verify_nav_more_section():
    more_link = driver.find_element(By.XPATH, "//span[@class='font-primary']")
    more_link.click()
    print("More link is active")
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
        By.XPATH, "//h1[contains(text(),'Blavity News is a community and platform for Black')]")))
    verify_more_email_section()
    verify_more_politics()
    more_link.click()
    verify_more_news()
    more_link.click()
    verify_more_op_ed()
    more_link.click()
    verify_more_write_a_story()
    more_link.click()
    verify_more_terms()
    more_link.click()
    verify_more_partner_with_us()
    more_link.click()
    verify_more_culture()
    more_link.click()
    verify_more_my_account()
    more_link.click()
    verify_more_careers()
    more_link.click()
    verify_more_life_style()
    more_link.click()
    verify_more_privacy_policies()
    more_link.click()
    verify_more_shop()
    more_link.click()
    verify_more_social_justice()
    more_link.click()
    verify_more_mastercard()
    more_link.click()
    verify_more_disclaimer_text()
    verify_more_instagram_link()
    verify_more_twitter_link()
    verify_more_facebook_link()
    verify_more_blavity_image()
    print("verified all links in more section.")


def verify_nav_bar_links():
    print("check whether each nav bar link is present and working, total 7 links")
    verify_nav_news_link()
    verify_nav_opinions_link()
    verify_nav_lifestyle_link()
    verify_nav_blavity_u_link()
    verify_submit_story()
    verify_sign_up_link()
    verify_nav_search_bar()
    print("All 7 links :- News, Op-Eds, Lifestyle, BlavityU, Submit a "
          "Story, Sign-Up and search bar are working as expected.")
    verify_nav_more_section()


def verify_footer_presence():
    time.sleep(3)
    footer_news_page = driver.find_element(By.XPATH,
                                           "//footer[@class='app-footer text-center text-desktop-left text-white']")
    actions.move_to_element(footer_news_page).perform()
    if footer_news_page.is_displayed():
        print("footer section is displayed on news page")


def exit_browser():
    print("closing the browser instance")
    driver.quit()
