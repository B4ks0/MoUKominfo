# MoUKominfo Journalist Registration Portal

A Django-based web application for managing journalist registrations and verifications by the Ministry of Communication and Information Technology (Kominfo).

## Overview

This platform acts as a bridge between journalists and the Ministry, facilitating an efficient registration and verification process. It allows journalists to submit required documents and data, which are then reviewed by Kominfo staff via a dedicated admin panel.

## Key Features

### For Journalists (Public)
*   **Multi-step Registration**: A user-friendly form gathering personal data, media organization details, and required documents (Cooperation letters, ID cards, Company Profile, etc.).
*   **Application Tracking**: Automatically generates a unique "Nomor Permohonan" (NRP) for each submission.
*   **Status Check**: Applicants can verify the status of their application (Pending, Approved, Rejected) using their NRP.

### For Admins (Kominfo Staff)
*   **Dashboard**: High-level summary of total registrations and verification statuses.
*   **Management & Verification**:
    *   Paginated list of all applications with filtering and search capabilities.
    *   Detailed view to review uploaded documents and applicant data.
    *   Ability to manually Approve or Reject applications.
*   **Reporting**: CSV export functionality for all registration data, including NRPs.
*   **Auto-Verify**: Feature to bulk approve pending applications for efficiency.

## System Flow

1.  **Registration**: Journalist fills out the multi-step form at `/register/`.
2.  **Processing**: System generates an NRP and marks the status as `pending`.
3.  **Review**: Admin logs in, reviews the submission, and updates the status.
4.  **Feedback**: Journalist checks their status using the NRP on the status page.

## Technical Stack

*   **Backend**: Django Framework (Python)
*   **Frontend**: Bootstrap 5 (Responsive Design), Custom CSS/JS
*   **Database**: SQLite (Default) - easily swappable for PostgreSQL/MySQL
*   **Feature Set**:
    *   Modular App Structure (`pendaftaran`, `admin_panel`)
    *   Django Paginator for efficient data listing
    *   File Storage handling for document uploads
    *   Secure Admin Authentication

## Installation and Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/B4ks0/MoUKominfo.git
    cd MoUKominfo
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5.  Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6.  Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

*   **Public Access**: Visit `http://localhost:8000/register/` to view the registration form.
*   **Admin Access**: Visit `http://localhost:8000/admin-panel/` and log in with your superuser/staff credentials.

## License

This project is licensed under the MIT License.
