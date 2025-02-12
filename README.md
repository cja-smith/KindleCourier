# README

# KindleCourier

Pull top stories from news sites (currently the Guardian) and have them delivered to your Kindle

---

## Setup

1. **Clone the repository**  
   ```commandline
   git clone https://github.com/yourusername/KindleCourier.git
   cd KindleCourier```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure credentials**
* Get a [Guardian API key](https://open-platform.theguardian.com/access/)
* Copy the environment template:
   ```bash
   cp .env.example .env
   ```
* Edit .env with your details:
   ```bash
  # Email settings
   EMAIL_ADDRESS='your_email@gmail.com'
   EMAIL_PASSWORD='your_email_password' # Use "App Passwords" for Gmail  
   KINDLE_EMAIL = 'sample@kindle.com'
   SMTP_HOST='smtp.yourhost.com'
   SMTP_PORT=587 # Usually 587 for TLS

   # API settings
   GUARDIAN_API_KEY=''
   ```
  (Tip: Use "App Passwords" for Gmail in step 2.)

4. **Run**
   ```bash
   python main.py
   ```

## Usage
TBD
