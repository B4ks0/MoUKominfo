# MoUKominfo Website Overview

This website is a Django-based portal aimed at managing journalist registrations and their verification process by the Ministry of Communication and Information Technology (Kominfo).

---

## Core Functionality

### 1. Journalist Registration (Pendaftaran Wartawan)
- Allows journalists to register by submitting their personal data and uploading required documents.
- Registration form uses a multi-step interface:
  - **Step 1: Personal Information** - Captures data like full name, media organization, position, email, phone number, and address.
  - **Step 2: Document Uploads** - Upload various required documents including cooperation letters, company profile, editorial composition, ID cards, and other supporting files.
- Upon successful form submission, a unique "Nomor Permohonan" (NRP) is generated and issued to the applicant.
- Applicants can check the status of their registration by NRP via a dedicated status check page.

### 2. Admin Panel
- Restricted to staff users for managing journalist registrations.
- Provides key views:
  - **Dashboard:** Overview of total registrations and their approval status.
  - **Manage:** Paginated listing of registrations with filtering and search capabilities. Displays all applicant details along with the NRP.
  - **Verify:** Detailed view for individual registrations to review data and uploaded documents; allows updating the verification status (pending, approved, rejected).
  - **Report:** Displays a paginated listing similar to manage, with options to export the registrations data as CSV, including NRP.
  - **Auto Verify:** Provides an interface to auto-approve all pending applications (simple bulk operation).
- CSV export capability includes all applicant information and the assigned NRP for record keeping.

### 3. URL Routing and View Logic
- The site is divided into modular Django apps, e.g., `pendaftaran` handles the registration workflow and status checking; `admin_panel` handles staff management.
- URLs are namespaced for clarity and separation of concerns.
- The admin views enforce staff-only access using Django decorators (`login_required`, `user_passes_test`).

### 4. Template Details
- Utilizes Django template inheritance for consistent page layouts.
- Includes multi-step forms with progress indicators and client-side validation.
- Shows statuses with colored badges for visual clarity.
- Uses dynamic URL reversal for linking, ensuring reliable navigation.

### 5. Data Model (Summary)
- Journalists (Wartawan) data includes personal info, media affiliation, uploaded documents, status, assigned NRP, and timestamps.
- Status field tracks application progress: pending, approved, or rejected.

---

## How the Website Works (Flow)

1. A journalist visits the registration page and fills out the multi-step form with required data and files.
2. Upon submission, the website generates an NRP and saves the registration with a `pending` status.
3. The journalist can check the status of their application with the NRP on the status page.
4. Staff users log into the admin panel to view/manage registrations.
5. Admin users review detailed data and documents, changing statuses as appropriate.
6. Admin can export all registration data including NRPs for reporting.
7. Optionally, admin users can bulk approve pending applications with the auto-verify feature.

---

## Technical Stack

- Backend: Django framework (Python)
- Templating: Django templating system with Bootstrap 5 for responsive UI styling.
- Authentication: Django's built-in authentication to secure the admin panel.
- File storage: Media uploads stored and served from the configured media directory.
- Pagination: Django Paginator used for list views.
- Validation: Forms leverage server-side and client-side validation.
- URL Routing: Organized with app namespaces and meaningful URL naming.

---

## Summary

This website efficiently facilitates the complete lifecycle of journalist registration, document verification, and administration by Kominfo staff. It balances user-friendly multi-step forms for applicants with powerful management tools for administrators, including reporting and bulk approval.

The use of NRP throughout ensures consistent tracking of each application from submission to final status.

---

For further questions or enhancements, please refer to the code documentation and Django app structures.
