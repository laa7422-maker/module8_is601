# tests/test_e2e.py
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def page():
    """Launch a headless browser once for all E2E tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        pg = browser.new_page()
        yield pg
        browser.close()


# ---------- ADD (happy path) ----------
def test_add_e2e(page):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "5")
    page.click("button:has-text('Add')")
    page.wait_for_selector("#result")
    assert "15" in page.inner_text("#result")


# ---------- SUBTRACT ----------
def test_subtract_e2e(page):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "5")
    page.click("button:has-text('Subtract')")
    page.wait_for_selector("#result")
    assert "5" in page.inner_text("#result")


# ---------- MULTIPLY ----------
def test_multiply_e2e(page):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "5")
    page.click("button:has-text('Multiply')")
    page.wait_for_selector("#result")
    assert "50" in page.inner_text("#result")


# ---------- DIVIDE (happy path) ----------
def test_divide_e2e(page):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "5")
    page.click("button:has-text('Divide')")
    page.wait_for_selector("#result")
    assert "2" in page.inner_text("#result")


# ---------- DIVIDE BY ZERO (error path) ----------
def test_divide_by_zero_e2e(page):
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "0")
    page.click("button:has-text('Divide')")
    page.wait_for_selector("#result")
    assert "Cannot divide by zero" in page.inner_text("#result")
