# Web-IDE: All-In-One Development & Content Creation Platform

![Version](https://img.shields.io/badge/version-3.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)

A comprehensive, browser-based integrated development environment combining code editing, server simulation, and content generation in one powerful platform.

## 🌟 Features

### 💻 IDE Module
- **Monaco Editor** - Full-featured code editor with syntax highlighting for 50+ languages
- **IntelliSense** - Intelligent code completion and suggestions
- **File Explorer** - Complete file management system
- **Integrated Terminal** - WebSocket-based bash terminal
- **Git Integration** - Init, commit, push, pull operations
- **Code Execution** - Run Python, Java, JavaScript, Bash directly
- **Search & Replace** - Global find and replace with regex support
- **Problems Panel** - Error and warning diagnostics

### 🖥️ Server Simulator Module
- **Container Management** - Create, start, stop containers
- **Service Management** - Manage nginx, mysql, redis, ssh services
- **System Monitoring** - Real-time CPU, memory, disk monitoring
- **Health Checks** - System status and diagnostics
- **Process Management** - Execute and monitor processes

### 🎬 Video Generator Module
- **Project Management** - Organize video projects
- **Templates** - Slideshow, presentation, tutorial, animation
- **Scene Management** - Add and arrange scenes with transitions
- **Audio Integration** - Background music and voiceover support
- **Effects & Transitions** - Fade, slide, zoom, rotate effects
- **Video Rendering** - Export to MP4 in multiple resolutions

### 🎨 Image Generator Module
- **AI Image Generation** - Multiple models (Stable Diffusion, DALL-E, Midjourney)
- **Style Presets** - Photorealistic, artistic, cartoon, sketch, abstract
- **Image Variations** - Generate variations from existing images
- **Upscaling** - Enhance image resolution (2x, 4x, 8x)
- **Batch Processing** - Generate multiple images at once
- **Project Organization** - Organize images by project

### 📚 Book Generator Module
- **Book Management** - Create and manage books
- **Templates** - Novel, technical, educational, business templates
- **Chapter Management** - Add, edit, delete chapters
- **Cover Design** - Customizable book covers
- **Styling** - 5 professional styles (classic, technical, modern, professional, educational)
- **Export Formats** - PDF and EPUB generation
- **Statistics** - Word count, page estimation, reading time

### 🗄️ Database Manager Module
- **Connection Management** - Multiple MySQL connections with pooling
- **Database Browser** - Browse databases, tables, columns
- **Query Editor** - Execute SQL with syntax highlighting
- **Query History** - Last 100 queries with execution details
- **Data Export** - Export table data to CSV
- **Performance Monitoring** - Execution time tracking

### 📊 Dashboard Module
- **Project Overview** - View all projects and assets
- **Quick Statistics** - Project counts, storage usage
- **Module Overview** - Status of all modules
- **Getting Started** - Onboarding guide
- **System Status** - API, database, WebSocket, storage status

---

## 🚀 Quick Start

### Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/web-ide.git
cd web-ide

# Copy environment file
cp .env.example .env

# Start with Docker Compose
docker-compose up -d

# Access at http://localhost:3000
```

### Direct Installation

```bash
# Install dependencies
npm install

# Build frontend
npm run build

# Start server
npm start
```

### Development Mode

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

---

## 📋 Requirements

### Minimum
- Node.js 22+
- MySQL 8.0+
- 2GB RAM
- 10GB storage

### Recommended
- Node.js 22+
- MySQL 8.0+
- 4GB+ RAM
- 50GB+ storage
- Docker & Docker Compose

---

## 🏗️ Architecture

### Technology Stack

| Layer | Technology |
|:---|:---|
| **Frontend** | React 18 + Vite |
| **Backend** | Express.js + Node.js |
| **Real-time** | Socket.io |
| **Database** | MySQL2 |
| **Authentication** | JWT |
| **Styling** | CSS3 + Dark Theme |
| **Container** | Docker |

### Project Structure

```
web-ide/
├── src/
│   ├── components/          # Shared UI components
│   ├── modules/             # Independent feature modules
│   ├── pages/               # Page layouts
│   └── styles/              # CSS files
├── server.js                # Express server
├── environment-manager.js   # Language execution
├── db-manager.js            # Database operations
├── linux-server-simulator.js # Server simulation
├── video-generator.js       # Video generation
├── image-generator.js       # Image generation
├── book-generator.js        # Book generation
├── Dockerfile               # Docker image
├── docker-compose.yml       # Docker services
└── package.json             # Dependencies
```

---

## 🔐 Security

- **JWT Authentication** - Secure token-based authentication
- **Password Hashing** - bcryptjs for secure password storage
- **User Isolation** - Each user has isolated workspace
- **Input Validation** - All inputs validated server-side
- **CORS Protection** - Cross-origin requests controlled
- **Environment Variables** - Sensitive data in .env

---

## 📚 Usage

### Default Credentials

```
Username: testuser
Password: password123
```

### Creating a New User

```bash
# Access the registration page at /register
# Or use the API
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
    -d '{"username":"newuser","password":"password123"}'
    ```

    ### API Documentation

    See [API_DOCS.md](./API_DOCS.md) for complete API reference.

    ---

    ## 🐳 Docker Deployment

    ### Build Image

    ```bash
    docker build -t web-ide:latest .
    ```

    ### Run Container

    ```bash
    docker run -p 3000:3000 \
      -e JWT_SECRET=your-secret \
        -e MYSQL_HOST=mysql \
          web-ide:latest
          ```

          ### Docker Compose

          ```bash
          docker-compose up -d
          docker-compose logs -f
          docker-compose down
          ```

          ---

          ## 📦 Deployment

          ### Production Deployment

          See [DEPLOYMENT.md](./DEPLOYMENT.md) for comprehensive deployment guide covering:
          - Docker deployment
          - Direct Node.js deployment
          - Cloud deployment (AWS, Heroku, DigitalOcean)
          - Security configuration
          - Monitoring and logging
          - Continuous deployment

          ### Environment Variables

          ```bash
          # Copy and configure
          cp .env.example .env

          # Key variables
          NODE_ENV=production
          PORT=3000
          JWT_SECRET=your-secret-key
          MYSQL_HOST=localhost
          MYSQL_USER=root
          MYSQL_PASSWORD=root
          MYSQL_DATABASE=web_ide
          ```

          ---

          ## 🧪 Testing

          ### Run Tests

          ```bash
          npm test
          ```

          ### Load Testing

          ```bash
          # Install Apache Bench
          sudo apt-get install apache2-utils

          # Run load test
          ab -n 1000 -c 10 http://localhost:3000/
          ```

          ---

          ## 🔄 Development

          ### Development Server

          ```bash
          npm run dev
          ```

          ### Build Frontend

          ```bash
          npm run build
          ```

          ### Format Code

          ```bash
          npm run format
          ```

          ### Lint Code

          ```bash
          npm run lint
          ```

          ---

          ## 📊 Performance

          ### Optimization Tips

          1. **Enable Caching** - Use Redis for session caching
          2. **Database Indexing** - Create indexes on frequently queried columns
          3. **Frontend Optimization** - Minify and compress assets
          4. **Load Balancing** - Use Nginx for load distribution
          5. **CDN** - Serve static assets from CDN

          ### Benchmarks

          | Operation | Time |
          |:---|:---|
          | Code Execution | < 1s |
          | Image Generation | 10-60s |
          | Video Rendering | 1-5m |
          | PDF Generation | 5-30s |
          | Database Query | < 1s |

          ---

          ## 🆘 Troubleshooting

          ### Common Issues

          **Port 3000 already in use**
          ```bash
          lsof -i :3000
          kill -9 <PID>
          ```

          **Database connection error**
          ```bash
          # Check MySQL service
          sudo systemctl status mysql
          sudo systemctl restart mysql
          ```

          **Out of memory**
          ```bash
          node --max-old-space-size=4096 server.js
          ```

          See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for more solutions.

          ---

          ## 📝 Documentation

          - [API Documentation](./API_DOCS.md)
          - [Deployment Guide](./DEPLOYMENT.md)
          - [Architecture Guide](./ARCHITECTURE.md)
          - [Contributing Guide](./CONTRIBUTING.md)
          - [Troubleshooting](./TROUBLESHOOTING.md)

          ---

          ## 🤝 Contributing

          Contributions are welcome! Please follow these steps:

          1. Fork the repository
          2. Create a feature branch (`git checkout -b feature/amazing-feature`)
          3. Commit changes (`git commit -m 'Add amazing feature'`)
          4. Push to branch (`git push origin feature/amazing-feature`)
          5. Open a Pull Request

          ---

          ## 📄 License

          This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

          ---

          ## 🙏 Acknowledgments

          - Monaco Editor - Code editing
          - Socket.io - Real-time communication
          - Express.js - Web framework
          - React - Frontend framework
          - MySQL - Database

          ---

          ## 📞 Support

          - **Documentation**: See [docs](./docs) folder
          - **Issues**: [GitHub Issues](https://github.com/yourusername/web-ide/issues)
          - **Discussions**: [GitHub Discussions](https://github.com/yourusername/web-ide/discussions)
          - **Email**: support@web-ide.com

          ---

          ## 🗺️ Roadmap

          - [ ] Real-time collaboration
          - [ ] Advanced AI features
          - [ ] Mobile app
          - [ ] Plugin system
          - [ ] Advanced analytics
          - [ ] Team management
          - [ ] Version control
          - [ ] Backup & restore

          ---

          ## 📈 Statistics

          - **7 Independent Modules**
          - **50+ API Endpoints**
          - **50+ Supported Languages**
          - **100+ Components**
          - **5000+ Lines of Code**

          ---

          ## 🎯 Use Cases

          - **Full-stack Development** - Code, test, deploy
          - **Content Creation** - Videos, images, books
          - **Learning & Education** - Interactive coding tutorials
          - **DevOps** - Server simulation and management
          - **Data Analysis** - Database management and queries
          - **Digital Publishing** - Book and content creation
          - **Automation** - Script development and execution

          ---

          ## 🚀 Version History

          ### v3.0.0 (Current)
          - Complete All-In-One Platform
          - 7 independent modules
          - Modular architecture
          - Production-ready deployment

          ### v2.0.0
          - Added Video, Image, Book generators
          - Database Manager
          - Server Simulator

          ### v1.0.0
          - Initial IDE release
          - Code editor
          - Terminal
          - File explorer

          ---

          **Web-IDE v3.0.0 - The Complete Development & Content Creation Platform** 🚀

          Made with ❤️ for developers and creators

          