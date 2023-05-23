這是一個方便我製作新程式使用的模板

簡單的簡化程式碼
def web(driver, timeout, locator_type, locator):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((locator_type, locator)))

driver = template.openchrome()

template.resetsystem(driver)