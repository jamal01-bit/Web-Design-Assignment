# Session Log - March 15, 2026

## 1. Image Styling Fixes
We addressed issues where images were either too large or being cropped on different monitors.

**Final Solution in `style.css`:**
```css
.page-img {
    width: 100%;       /* Makes image as wide as the text */
    height: auto;      /* Maintains aspect ratio (no stretching) */
    display: block;
    margin: 20px 0;    /* Aligns with text flow */
    border-radius: 8px; /* Modern rounded corners */
}
```
*   **Result**: Images now fill the width of the container without any cropping or distortion.

## 2. Form Logic Explanation (`take-action.html`)
We broke down the "Climate Contribution Survey" into conceptual sections:

### The Brains & GPS
*   **Action/Method**: Sends data to FormSubmit via a secure `POST` request.
*   **`_next`**: A hidden instruction that tells the server to redirect to `thank-you.html` after a successful submission.
*   **`_captcha`**: Set to `false` to skip the "I am not a robot" check for a faster user experience.

### The Structure
*   **`<fieldset>` & `<legend>`**: Used to group related questions (Transport, Lifestyle, Ideas) with a visible border and title.
*   **Radio Buttons**: Used for single-choice answers (Transport).
*   **Checkboxes**: Used for multiple-choice answers (Lifestyle).
*   **Textarea**: Used for long-form suggestions and ideas.

## 3. Redirect Logic
The "Thank You" page redirect works because the FormSubmit service looks for the `_next` hidden input field. Once it finishes processing the email, it sends the browser's "GPS" to the URL provided in that field's value.
