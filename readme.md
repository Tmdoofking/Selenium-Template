這是一個方便我製作新程式使用的模板

簡單的簡化程式碼

    def web(driver, timeout, locator_type, locator):

        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((locator_type, locator)))

**locator_type**

By.ID: 使用元素的 id 屬性進行定位。例如：By.ID("myElement")

By.NAME: 使用元素的 name 屬性進行定位。例如：By.NAME("myElement")

By.CLASS_NAME: 使用元素的 class 屬性進行定位。例如：By.CLASS_NAME("myElement")

By.TAG_NAME: 使用元素的標籤名稱進行定位。例如：By.TAG_NAME("div")

By.LINK_TEXT: 使用超連結文字進行定位。例如：By.LINK_TEXT("Click Here")

By.PARTIAL_LINK_TEXT: 使用部分超連結文字進行定位。例如：By.PARTIAL_LINK_TEXT("Click")

By.XPATH: 使用 XPath 表達式進行定位。例如：By.XPATH("//input[@name='myElement']")

By.CSS_SELECTOR: 使用 CSS 選擇器進行定位。例如：By.CSS_SELECTOR("#myElement")

**模板可用程式**

driver = template.openchrome()

template.resetsystem(driver)
