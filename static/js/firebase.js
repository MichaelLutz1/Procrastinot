// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.0/firebase-app.js";
import { getMessaging, getToken } from "https://www.gstatic.com/firebasejs/9.1.0/firebase-messaging.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCvwluCZla7QWuNwgO5fY3ywkwFzRYkLKI",
  authDomain: "procrastinot-ad604.firebaseapp.com",
  projectId: "procrastinot-ad604",
  storageBucket: "procrastinot-ad604.appspot.com",
  messagingSenderId: "243654436505",
  appId: "1:243654436505:web:dbb9c864b971eac213ba08"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);
console.log(app, messaging)
getToken(messaging, { vapidKey: "BJ57RuEVa5BWTMCNiZP7mohmGsmY3sKLgrFQNd5zG-0m8J6G9IHkEZUAWng1VfyLEsqoLzdnutRuYn-RS-532gc" });
function requestPermission() {
  console.log('Requesting permission...');
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('Notification permission granted.');
    }
  })
}

