
# Tests

This document provides an overview of the automated UI tests implemented for the [AutomationExercise](https://www.automationexercise.com/) website using Python, Selenium WebDriver, Pytest, and Allure.

## Table of Contents

- [Login](#login)
- [Logout](#logout)
- [Signup](#signup)
- [Account Management](#account-management)
- [Products](#products)
- [Shopping Cart](#shopping-cart)
- [Search and Filter](#search-and-filter)
- [Checkout and Orders](#checkout-and-orders)
- [Contact Us](#contact-us)
- [Subscription](#subscription)

## Login

| ID | Test Case |
|---|---|
| T01 | Login with valid credentials |
| T02 | Login with unregistered email |
| T03 | Login with incorrect password |
| T04 | Login with empty email field |
| T05 | Login with empty password field |

## Logout

| ID | Test Case |
|---|---|
| T06 | Successful logout |

## Signup

| ID | Test Case |
|---|---|
| T07 | Successful signup with valid data |
| T08 | Signup with an existing email |
| T09 | Signup with invalid email format |
| T10 | Signup with empty name field |
| T11 | Signup with empty email field |

## Account Management

| ID | Test Case |
|---|---|
| T12 | Successful account deletion |

## Products

| ID | Test Case |
|---|---|
| T13 | Verify products page is displayed |
| T14 | Verify product details |
| T15 | Submit a review for a product |

## Shopping Cart

| ID | Test Case |
|---|---|
| T16 | Add product to cart and verify confirmation |
| T17 | Verify product information in cart |
| T18 | Verify product quantity and total price in cart |
| T19 | Delete product from cart |
| T20 | Add recommended product to cart |
| T21 | Verify cart contents after login |

## Search and Filter

| ID | Test Case |
|---|---|
| T22 | Search product by name |
| T23 | Search for a non-existent product |
| T24 | Filter products by brand |
| T25 | Filter products by category and subcategory |

## Checkout and Orders

| ID | Test Case |
|---|---|
| T26 | Complete purchase flow |
| T27 | Verify delivery address details in checkout |
| T28 | Download and verify invoice after purchase |

## Contact Us

| ID | Test Case |
|---|---|
| T29 | Submit the Contact Us form |

## Subscription

| ID | Test Case |
|---|---|
| T30 | Verify subscription on the home page |
| T31 | Verify subscription on the cart page |