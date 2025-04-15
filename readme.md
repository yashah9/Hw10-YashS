# Event Manager


## Features

- **User Registration & Authentication**
  - Users can register and authenticate via JWT tokens.
  - Roles such as ADMIN and MANAGER are supported with role-based access control.

- **Email Verification**
  - Users must verify their email to complete registration.
  - Email verification is managed using external email services like Mailtrap for testing.

- **Profile Management**
  - Users can set and update their profile information, including nickname, profile picture URL, and social media URLs.

- **Password Validation**
  - Strong password validation is enforced during registration and profile update.

- **Unique Username Validation**
  - The application ensures that all usernames (nicknames) are unique.


### Issues Solved


### 1. [JWT Token and Pytest Error](https://github.com/yashah9/Hw10-YashS/issues/1)
   - **Problem**: Login Authentication failed for users with ADMIN, MANAGER roles due to JWT token issues.
   - **Solution**: Fixed JWT token generation and authentication logic to correctly handle user roles during login.
   - **Pytest Errors**: Addressed various Pytest issues to ensure smooth testing of authentication and email verification.

### 2. [Nickname Mismatched in Register](https://github.com/yashah9/Hw10-YashS/issues/3)
   - **Problem**: There was a mismatch in the nickname provided during user registration.
   - **Solution**: Corrected the logic to ensure consistent nickname handling across the registration process.

### 3. [Password Validation](https://github.com/yashah9/Hw10-YashS/issues/7)
   - **Problem**: The application lacked proper password validation.
   - **Solution**: Implemented password strength validation to ensure security and user compliance.

### 4. [URL Validation](https://github.com/yashah9/Hw10-YashS/issues/5)
   - **Problem**: Invalid URLs could be provided in fields such as `profile_picture_url`, `linkedin_profile_url`, and `github_profile_url`.
   - **Solution**: Implemented URL validation to ensure that all URLs provided are valid and correctly formatted.

### 5. [Unverified Email Users](https://github.com/yashah9/Hw10-YashS/issues/9)
   - **Problem**: Users with unverified emails could update their profiles, leading to potential security issues.
   - **Solution**: Added a check to ensure that only verified email users can update their profile information.

### 6. [Unique Username (Nickname) Validation](https://github.com/yashah9/Hw10-YashS/issues/11)
   - **Problem**: Users could insert the same nickname, which was invalid.
   - **Solution**: Added unique nickname validation to prevent duplicate usernames during registration.


### Outcomes

This project allowed me to deepen my understanding of secure API development using FastAPI, particularly in implementing JWT-based authentication and role-based access control for roles like ADMIN and MANAGER. I resolved complex issues with token generation and user authentication that initially prevented certain users from logging in. Through this, I gained practical experience debugging critical components of a login system while ensuring that authentication aligned with the application’s business rules.

I also strengthened the application’s validation mechanisms by enforcing strong password policies and adding robust URL validation for user profiles. These enhancements not only improved the system’s overall security but also enhanced the user experience by reducing the chances of invalid data entry. Addressing inconsistencies like nickname mismatches during registration taught me the importance of data consistency and integrity across endpoints.

One major security improvement I worked on was preventing users with unverified emails from updating their profiles. This required integrating additional checks into the logic and helped me understand how small oversights can lead to larger security gaps. By resolving this, I ensured better control over user actions based on verification status—an important principle in secure system design.

Throughout the project, I became more confident in using tools like Pytest for automated testing, SQLAlchemy for database operations, and GitHub Issues for project tracking. The collaborative nature of the project emphasized the importance of writing clean, well-documented code and reinforced the value of feedback in a development workflow. This experience has equipped me with stronger skills in designing reliable, user-friendly, and secure backend systems.

## Image on dockerhub
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/16629b1e-c8b2-402d-96b6-a9726ef94dce" />
