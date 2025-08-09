# BaintMail1 - Secure Email Platform

A modern, privacy-first email application with AI-enhanced features and blockchain integration capabilities.

## 🚀 Features

- **Modern Dark UI**: Beautiful dark theme with BaintMail orange branding
- **AI-Powered**: Smart reply suggestions and email summarization
- **Real-time**: Live email updates and notifications
- **Secure**: End-to-end encryption ready architecture
- **Responsive**: Works on desktop and mobile devices
- **Web3 Ready**: Blockchain integration capabilities

## 📁 Project Structure

```
baintmail-deployment/
├── baintmail-frontend/     # React frontend application
├── baintmail-backend/      # Flask backend API
└── README.md              # This file
```

## 🛠️ Local Development Setup

### Prerequisites
- Node.js 20+ 
- Python 3.11+
- npm or yarn

### Frontend Setup
```bash
cd baintmail-frontend
npm install
npm run dev
```
The frontend will be available at `http://localhost:5174`

### Backend Setup
```bash
cd baintmail-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```
The backend API will be available at `http://localhost:5000`

## 🌐 Deployment Options

### Option 1: Frontend-Only Deployment (Recommended for Demo)
Deploy just the frontend to platforms like:
- Vercel
- Netlify
- GitHub Pages

### Option 2: Full-Stack Deployment
Deploy both frontend and backend to:
- Railway
- Render
- Heroku
- DigitalOcean App Platform

### Option 3: Self-Hosted
Deploy on your own server using:
- Docker
- PM2
- Nginx

## 🔧 Configuration

### Frontend Configuration
- API endpoint: Update `API_BASE_URL` in `src/api.js`
- Branding: Logo located in `public/1001292373.png`

### Backend Configuration
- CORS settings: Configured for `localhost:5174`
- Database: Currently using mock data (ready for real database integration)

## 🎨 Brand Guidelines

- **Primary Color**: #FF6B00 (BaintMail Orange)
- **Background**: #0D0D0D (Jet Black)
- **Secondary**: #1A1A1A (Charcoal Gray)
- **Typography**: Poppins (headings), Inter (body)

## 📱 Features Implemented

### Core Email Features
- ✅ Email composition and sending
- ✅ Email reading and management
- ✅ Real-time email updates
- ✅ Search functionality
- ✅ Folder organization
- ✅ Mark as read/unread

### AI Features
- ✅ Smart reply suggestions
- ✅ Email summarization (backend ready)
- ✅ Contextual responses

### UI/UX Features
- ✅ Dark mode interface
- ✅ Responsive design
- ✅ Smooth animations
- ✅ Professional branding
- ✅ Three-panel layout

## 🔮 Future Enhancements (Phase 2)

- Blockchain wallet integration
- Decentralized identity login
- BaintMail Playstore (mini apps)
- Encrypted file storage
- Voice/video messages
- Public BaintMail usernames

## 🤝 Contributing

This is a proprietary project for BaintMail. For development questions or feature requests, contact the BaintMail team.

## 📄 License

© 2025 BaintMail. All rights reserved.

---

**Built with ❤️ by the BaintMail Team**

