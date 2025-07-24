# Invoice Disclaimer Management

## Overview

This Odoo module allows you to manage customer-specific disclaimers that appear in the footer of invoices. Each customer can have a specific disclaimer assigned, and it will automatically appear on their invoices.

## Features

- **Customer-specific disclaimers**: Assign different disclaimers to different customers
- **Invoice footer display**: Disclaimers appear automatically in the footer of customer invoices
- **Easy management**: Simple interface to create and manage disclaimers
- **Multi-company support**: Disclaimers can be company-specific
- **Rich text support**: Use HTML formatting for disclaimers

## Installation

1. Copy this module to your Odoo addons directory
2. Update the app list: `Settings > Apps > Update Apps List`
3. Install the module: Search for "Invoice Disclaimer Management" and click Install

## Usage

### Creating Disclaimers

1. Go to `Accounting > Configuration > Invoice Disclaimers > Invoice Disclaimers`
2. Click "Create" to add a new disclaimer
3. Fill in:
   - **Name**: A descriptive name for the disclaimer
   - **Content**: The disclaimer text (supports HTML formatting)
   - **Company**: Select the company (if using multi-company setup)

### Assigning Disclaimers to Customers

1. Go to `Contacts` and open a customer record
2. Navigate to the "Invoice Settings" tab
3. Select the appropriate disclaimer from the "Invoice Disclaimer" field
4. Save the customer record

### Viewing Disclaimers on Invoices

1. Create or open an invoice for a customer with an assigned disclaimer
2. The disclaimer will automatically appear:
   - In the invoice form view (for reference)
   - In the printed/PDF invoice footer

## Technical Details

### Models

- `invoice.disclaimer`: Stores disclaimer content and metadata
- `res.partner`: Extended with `invoice_disclaimer_id` field
- `account.move`: Extended with computed `invoice_disclaimer` field

### Views

- Disclaimer management interface
- Customer form enhancement
- Invoice form enhancement
- Invoice report template modification

### Security

- **Users**: Can view disclaimers
- **Accountants**: Can create and edit disclaimers
- **Managers**: Full access including delete

## Customization

### Modifying Disclaimer Position

The disclaimer appears in the invoice footer by default. To change the position, modify the `reports/invoice_report.xml` file:

- Current position: Footer area
- Alternative: Move the XPath to position after different elements

### Styling

Customize the disclaimer appearance by modifying the CSS classes in the report template:

```xml
<div class="text-center" style="font-size: 10px; color: #666;">
    <!-- Disclaimer content -->
</div>
```

### Adding Fields

To add additional fields to disclaimers:

1. Extend the `invoice.disclaimer` model in `models/disclaimer.py`
2. Update the form view in `views/disclaimer_views.xml`
3. Update security rules if needed

## Dependencies

- `base`: Core Odoo functionality
- `account`: Accounting module for invoices
- `sale`: Sales module integration

## Support

For support and customization requests, please contact your Odoo developer or system administrator.

## Author

This module is maintained by: **Dino Herlmanbang**  
GitHub: [https://github.com/dinoherlambang](https://github.com/dinoherlambang)

## License

This module is provided as-is for Odoo 13 Community Edition.
