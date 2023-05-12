from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from RaisenCanesFn import click_next_button
from User_PPI import entry_code, user_name, user_address, user_city, user_state, user_zip, user_email, user_phone

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# # Use the driver to navigate to the Raising Cane's survey page
driver.get("https://www.raisingcanes.com/survey")

# Click the "English" button
english_button = driver.find_element(
    By.CSS_SELECTOR, "a[data-role='button'][class~='no-wrap'][class~='ui-link'][class~='ui-btn'][class~='ui-shadow'][class~='ui-corner-all']")
english_button.click()

# Enter a number in the first text box
entry_code_1 = driver.find_element(By.ID, "EntryCode1")
entry_code_1.send_keys(entry_code)

# Click the "Start" button
start_button = driver.find_element(
    By.CSS_SELECTOR, "input[type='submit'][value='Start'][data-inline='true']")
start_button.click()

# Click the "Begin Survey" button
begin_survey_button = driver.find_element(
    By.CSS_SELECTOR, "input[type='submit'][value='Begin Survey'][data-wrapper-class='so-button button-begin-survey so-button-begin-survey']")
begin_survey_button.click()

# Enter "10.59" in the text field
text_field = driver.find_element(
    By.ID, "Question_124200102196150218178053017029202235094208184212")
text_field.send_keys("10.59")

# Click the "Next" button
click_next_button(driver)

# Click the "Food/drink" radio button
food_drink_radio_button = driver.find_element(
    By.XPATH, "//label[@for='Question_217159188129148208162001078201237177025028062141_1']")
food_drink_radio_button.click()

click_next_button(driver)

# Wait for the user to manually select an item
time.sleep(5)  # replace 10 with the number of seconds you want to wait

click_next_button(driver)

# Wait for the user to manually select an item
time.sleep(5)  # replace 10 with the number of seconds you want to wait

click_next_button(driver)

# Click the "Once a week" button
once_a_week_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_157007034169081006105239042160105098245063223182_2']")
once_a_week_button.click()

click_next_button(driver)

# Click the "More than two years ago" radio button
more_than_two_years_ago_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_155183159184160009029083137210073137233022099235_1'][class~='ui-btn']")
more_than_two_years_ago_button.click()

click_next_button(driver)

once_a_week_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_123178142097242045169107177018058250017255111162_2']")
once_a_week_button.click()

click_next_button(driver)

# Click "The Box" checkbox
the_box_checkbox = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_139227082096244183198224192143116084091107161214_1']")
the_box_checkbox.click()

click_next_button(driver)

# Click on Chicken Fingers
chicken_fingers_checkbox = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_022154139220189068172239176029225218214033170044_1']")
chicken_fingers_checkbox.click()

# Click on French Fries
french_fries_checkbox = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_022154139220189068172239176029225218214033170044_3']")
french_fries_checkbox.click()

# Click on Sauce
sauce_checkbox = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_022154139220189068172239176029225218214033170044_6']")
sauce_checkbox.click()

click_next_button(driver)

# Click on 5 - Extremely Satisfied

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_154001027140065196142060057240085246036092011240_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_170115142014113204158053103109085062167084071234_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_109207061115098085053137110094079169178155106241_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_066201148252154014058236177067165056046034226070_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_039037009054186126001083156227128002049192097160_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_175193222053060185246196231185165237212052056086_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_028244181101007135007098142134003112024189031022_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)


radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_155243250208174119091247169252049175008186183176_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_106138226068014149130205179041178027083086024234_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_144078199190002154002113125159210191131012130099_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_041089255046114020074233176139027170176119056014_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_055240102107158144146238172101113133185133176044_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_170165103212068196124033106056128160012021139057_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_140114062052178181197027121240226154005040029168_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_234132007232253174168060171178084150064177025191_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_004226103068128212231237178197117160205145126021_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_177167017228105246232225249056105074176071171062_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_169006112175215214029233232223156160134185008107_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_169085229181238236153100087186040001248107023014_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_101097147141193186153084087182128071135065192085_5'][class~='ui-btn']")
radio_button.click()

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_234166199058241051078137021007062208225030227003_5'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_185005065236031205217162153051009115036221207006_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_081153229106124135042118019022031205083047019007_2'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_131180165211225246032148031129086045230242255153_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_051121214047111130015009099186072163059034202237_2'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

text_area = driver.find_element(
    By.ID, "Question_120094177164234154161238156156125236252076167165")
text_area.send_keys("Flawless service")

click_next_button(driver)


radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_086086165083248225177239104225026238052212245176_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_220095182052028147103029189008106007195061079139_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_020095200220071134235110039250113148191198037203_4'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_117022134211065218248149163127123140195245173129_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_070190027204146148050006145139112039053089084047_2'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_230029092078058163081082110241087105053221175014_2'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

radio_button = driver.find_element(
    By.CSS_SELECTOR, "label[for='Question_107188186165216157160019045226147053042253102237_1'][class~='ui-btn']")
radio_button.click()

click_next_button(driver)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[0].Response")
text_area.send_keys(user_name)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[1].Response")
text_area.send_keys(user_address)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[2].Response")
text_area.send_keys(user_city)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[3].Response")
text_area.send_keys(user_state)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[4].Response")
text_area.send_keys(user_zip)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[5].Response")
text_area.send_keys(user_email)

text_area = driver.find_element(
    By.ID, "Questions[0].CustomFields[6].Response")
text_area.send_keys(user_phone)

# click_next_button(driver)

# Wait for the user to press Enter before closing the window
input("Press Enter to close the window...")

# Close the browser window
driver.quit()
