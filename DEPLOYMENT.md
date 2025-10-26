# Web-IDE Deployment Guide

## 🚀 Overview

Web-IDE is a complete All-In-One Development & Content Creation Platform ready for production deployment. This guide covers various deployment options.

---

## 📋 Prerequisites

- Docker & Docker Compose (for containerized deployment)
- Node.js 22+ (for direct deployment)
- MySQL 8.0+ (if not using Docker)
- 2GB RAM minimum
- 10GB storage minimum

---

## 🐳 Docker Deployment (Recommended)

### Quick Start

1. **Clone or download the project**
   ```bash
   cd web-ide
   ```

2. **Create .env file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - URL: `http://localhost:3000`
   - Default user: `testuser` / `password123`

### Docker Compose Services

| Service | Port | Purpose |
|:---|:---|:---|
| web-ide | 3000 | Main application |
| mysql | 3306 | Database |
| redis | 6379 | Cache (optional) |

### Useful Docker Commands

```bash
# View logs
docker-compose logs -f web-ide

# Stop services
docker-compose down

# Rebuild images
docker-compose up -d --build

# Execute command in container
docker-compose exec web-ide npm run build

# View running containers
docker-compose ps
```

---

## 🖥️ Direct Node.js Deployment

### Prerequisites

```bash
# Install Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install MySQL
sudo apt-get install -y mysql-server

# Install PM2 globally
npm install -g pm2
```

### Installation Steps

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Build frontend**
   ```bash
   npm run build
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Start with PM2**
   ```bash
   pm2 start server.js --name "web-ide"
   pm2 save
   pm2 startup
   ```

5. **Access the application**
   - URL: `http://localhost:3000`

### PM2 Management

```bash
# View status
pm2 status

# View logs
pm2 logs web-ide

# Restart
pm2 restart web-ide

# Stop
pm2 stop web-ide

# Delete
pm2 delete web-ide
```

---

## ☁️ Cloud Deployment

### AWS EC2

1. **Launch Ubuntu 22.04 instance**
   - Instance type: t3.medium or larger
   - Storage: 20GB minimum

2. **SSH into instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Follow Direct Node.js Deployment steps**

4. **Setup Nginx reverse proxy**
   ```bash
   sudo apt-get install -y nginx
   sudo systemctl start nginx
   ```

5. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:3000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

### Heroku

1. **Install Heroku CLI**
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Add MySQL add-on**
   ```bash
   heroku addons:create cleardb:ignite
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### DigitalOcean App Platform

1. **Connect GitHub repository**
2. **Configure environment variables**
3. **Set build command**: `npm install && npm run build`
4. **Set run command**: `node server.js`
5. **Deploy**

---

## 🔒 Security Configuration

### Environment Variables

```bash
# Change these in production!
JWT_SECRET=your-very-secure-random-string
MYSQL_PASSWORD=your-strong-password
```

### SSL/TLS Certificate

```bash
# Using Let's Encrypt with Certbot
sudo apt-get install -y certbot python3-certbot-nginx
sudo certbot certonly --nginx -d your-domain.com
```

### Firewall Configuration

```bash
# Allow only necessary ports
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### Database Security

```bash
# Create non-root MySQL user
mysql -u root -p
CREATE USER 'web_ide'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON web_ide.* TO 'web_ide'@'localhost';
FLUSH PRIVILEGES;
```

---

## 📊 Monitoring & Logging

### PM2 Monitoring

```bash
# Install PM2 monitoring
pm2 install pm2-auto-pull

# View dashboard
pm2 monit
```

### Log Management

```bash
# View application logs
pm2 logs web-ide

# Rotate logs
pm2 install pm2-logrotate
```

### Database Backups

```bash
# Automatic daily backup
0 2 * * * mysqldump -u root -p'password' web_ide > /backups/web_ide_$(date +\%Y\%m\%d).sql
```

---

## 🔄 Continuous Deployment

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /app/web-ide
            git pull origin main
            npm install
            npm run build
            pm2 restart web-ide
```

---

## 🧪 Testing Before Production

### Health Check

```bash
curl http://localhost:3000/api/server/health
```

### Load Testing

```bash
# Install Apache Bench
sudo apt-get install -y apache2-utils

# Run load test
ab -n 1000 -c 10 http://localhost:3000/
```

---

## 📈 Performance Optimization

### Nginx Caching

```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=web_ide_cache:10m;

location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    proxy_cache web_ide_cache;
    proxy_cache_valid 200 30d;
    add_header X-Cache-Status $upstream_cache_status;
}
```

### Database Optimization

```sql
-- Create indexes
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_files_user_id ON files(user_id);
CREATE INDEX idx_projects_user_id ON projects(user_id);
```

---

## 🆘 Troubleshooting

### Port Already in Use

```bash
# Find process using port 3000
lsof -i :3000

# Kill process
kill -9 <PID>
```

### Database Connection Error

```bash
# Check MySQL service
sudo systemctl status mysql

# Restart MySQL
sudo systemctl restart mysql

# Test connection
mysql -u root -p -h localhost
```

### Out of Memory

```bash
# Increase Node.js heap
node --max-old-space-size=4096 server.js

# Or with PM2
pm2 start server.js --max-memory-restart 1G
```

---

## 📞 Support & Maintenance

### Regular Tasks

- [ ] Monitor disk space
- [ ] Check database backups
- [ ] Review error logs
- [ ] Update dependencies
- [ ] Security patches
- [ ] Performance monitoring

### Update Procedure

```bash
# Pull latest changes
git pull origin main

# Install new dependencies
npm install

# Rebuild frontend
npm run build

# Restart application
pm2 restart web-ide
```

---

## 📊 System Requirements

### Minimum

- CPU: 1 core
- RAM: 2GB
- Storage: 10GB
- Bandwidth: 1Mbps

### Recommended

- CPU: 2+ cores
- RAM: 4GB+
- Storage: 50GB+
- Bandwidth: 10Mbps+

### High-Traffic

- CPU: 4+ cores
- RAM: 8GB+
- Storage: 100GB+
- Load balancer: Yes
- CDN: Yes

---

## 🎯 Deployment Checklist

- [ ] Environment variables configured
- [ ] SSL/TLS certificate installed
- [ ] Database backups configured
- [ ] Firewall rules applied
- [ ] Monitoring setup
- [ ] Log rotation configured
- [ ] Health checks passing
- [ ] Load testing completed
- [ ] Security audit done
- [ ] Documentation updated

---

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Node.js Best Practices](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
- [MySQL Security](https://dev.mysql.com/doc/refman/8.0/en/security.html)
- [PM2 Documentation](https://pm2.keymetrics.io/)

---

## 📄 License

MIT License - Open source and free to use

---

**Web-IDE v3.0.0 - Production Ready** 🚀

