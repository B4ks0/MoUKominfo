# MoUKominfo Journalist Registration Portal

This is a Django-based web application for managing journalist registrations and verifications by the Ministry of Communication and Information Technology (Kominfo).

## Features

- Multi-step registration form for journalists to submit personal data and required documents.
- Automatically generates a unique application number ("Nomor Permohonan" / NRP) for each registration.
- Allows journalists to check the status of their application via the NRP.
- Admin panel for Kominfo staff to manage registrations:
  - Dashboard with summary statistics.
  - Manage page to view, search, and filter applications.
  - Verify page to review and update application statuses.
  - Report page with CSV export of registration data.
  - Auto-verify feature to bulk approve pending applications.

## Technical Details

- Backend: Django Framework with modular apps.
- Authentication: Django's user authentication for admin access.
- Pagination: Django Paginator for list views.
- File Uploads: Handles multiple required document uploads per registration.
- URL Routing: Uses namespaced URLs for clear separation of public and admin routes.
- Templating: Django templates with Bootstrap 5 styles for responsive UI.
- Validation: Client-side checks on multi-step forms and server-side form validations.
- Status tracking with color-coded badges for visual clarity.

## Installation and Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   ```

2. Create and activate a Python virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```
   python manage.py migrate
   ```

5. Run the development server:

   ```
   python manage.py runserver
   ```

6. Access the site:

   - Public registration pages: `http://localhost:8000/register/`
   - Admin panel: `http://localhost:8000/admin-panel/`

## Usage

- Journalists register via the multi-step form.
- Admin staff login to the admin panel to manage and verify registrations.
- Status changes trigger updates visible to applicants checking via NRP.

## Contributing

Contributions, issues, and feature requests are welcome. Please open issues and pull requests via GitHub.

## License

This project is licensed under the MIT License.

---

For detailed explanation of the website functionality, see [DOCUMENTATION_WEBSITE_OVERVIEW.md](DOCUMENTATION_WEBSITE_OVERVIEW.md).
