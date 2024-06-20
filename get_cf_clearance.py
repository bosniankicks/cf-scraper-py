from undetected_playwright.sync_api import sync_playwright
import sys
import json
import time

def get_cf_clearance_cookie(url):
    browser = None
    used_user_agent = None
    cf_clearance = None

    try:
        with sync_playwright() as p:
            args = ["--disable-blink-features=AutomationControlled"]
            browser = p.chromium.launch(args=args, headless=False, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
            context = browser.new_context()
            page = context.new_page()

            used_user_agent = page.evaluate("navigator.userAgent")
            page.goto(url)
            time.sleep(5)

            cookies = context.cookies()
            cf_clearance = next((cookie['value'] for cookie in cookies if cookie['name'] == 'cf_clearance'), None)

    except Exception as e:
        print(f"Error during Playwright execution: {e}", file=sys.stderr)
    finally:
        if browser:
            try:
                browser.close()
            except Exception as e:
                print(f"Error while closing the browser: {e}", file=sys.stderr)

    result = {
        "cf_clearance": cf_clearance,
        "user_agent": used_user_agent
    }
    print(json.dumps(result, indent=4))  # Pretty-print the JSON result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python get_cf_clearance.py <url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    get_cf_clearance_cookie(url)
