const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();

// 환경 변수 로드
const PORT = process.env.PORT || 3000;
const MONGO_URI = process.env.MONGO_URI;

// MongoDB 연결
// mongoose.connect('mongodb://root:passw0rd@9.30.245.200:27017')
mongoose.connect(MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('MongoDB Connected'))
.catch(err => console.error('MongoDB connection error:', err));

// 미들웨어 설정
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// 라우트 설정
app.use('/api/users', require('./routes/users'));

// 서버 시작
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
