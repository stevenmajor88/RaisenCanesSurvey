from selenium.webdriver.common.by import By


def click_next_button(driver):
    next_button = driver.find_element(
        By.CSS_SELECTOR, "input[type='submit'][value='Next'][data-icon='forward'][data-iconpos='right'][data-wrapper-class='so-button button-next so-button-next']")
    next_button.click()
