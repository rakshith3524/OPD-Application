**Angular Medical Appointment Management System**

This project is an Angular-based web application designed to manage medical appointments, patient registrations, and doctor dashboards. It includes various components and services to facilitate these functionalities.

**Table of Contents**

- Installation
- Usage
- Components
- Services
- Guards
- Testing

**Installation**

1. Clone the repository:
  - git clone &lt;repository-url&gt;

2. Navigate to the project directory:
   - cd &lt;project-directory&gt;

3. Install dependencies:
   - npm install

**Usage**

1. Start the development server:
  - ng serve
2. Open your browser and navigate to "http://localhost:4200/"

**Components**

- **ProfileComponent**: User login.
- **ProfileListComponent**: Lists all profiles(Patient or Staff).
- **StartpageComponent**: The landing page.
- **PatientnavComponent**: Navigation for patients.
- **PatientloginComponent**: Login form for patients.
- **PatientsignupComponent**: Signup form for patients.
- **StaffprofileComponent**: Displays staff profile.
- **StaffStartpageComponent**: Landing page for staff.
- **BookAppointmentComponent**: Form to book appointments.
- **PatientAppointmentManagementComponent**: Manages patient appointments.
- **DoctorDashboardComponent**: Dashboard for doctors.
- **FrontpageComponent**: The main front page.
- **PatientRegManagementComponent**: Manages patient registrations.
- **StaffAppManagementComponent**: Manages staff appointments.
- **DocnavComponent**: Navigation for doctors.
- **LogoutComponent**: Handles user logout.
- **FeedbackComponent**: Collects user feedback.

**Services**

- **AppointmentService**: Manages appointment-related operations.
- **DoctorService**: Manages doctor-related operations.
- **ProfileService**: Manages user profiles.
- **RegistrationService**: Handles patient registrations.
- **SharingService**: Shares data across components.

**Guards**

- **adminGuard**: Protects admin routes.
- **authGuard**: Protects authenticated routes.

**Testing**

Run unit tests:

ng test
