<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="logo">
        <img src="@/assets/text-logo.svg" alt="Text Logo" />
      </div>
      <p class="description">
        Привет! "Pet Locate" - это простой и удобный сервис, который помогает с поиском ваших питомцев
      </p>
      <div class="toggle">
        <label>
          <input type="radio" v-model="authMode" value="Вход" /> Вход
        </label>
        <label>
          <input type="radio" v-model="authMode" value="Регистрация" /> Регистрация
        </label>
      </div>
      <form @submit.prevent="handleFormSubmit" class="auth-form">
        <template v-if="authMode === 'Регистрация'">
          <template v-if="!useEmail">
            <div class="form-item">
              <input v-model="form.phone" type="text" placeholder="Введите телефон" />
            </div>
            <div class="form-item" v-if="!codeSent">
              <button type="button" class="primary-button" @click="sendCode" :disabled="sendingCode">
                {{ sendingCode ? 'Отправка...' : 'Выслать код' }}
              </button>
            </div>
            <div class="form-item" v-if="codeSent">
              <input v-model="form.verificationCode" type="text" placeholder="Введите код" />
            </div>
            <div class="form-item" v-if="codeSent">
              <button type="button" class="primary-button" @click="verifyCode">
                Подтвердить код
              </button>
            </div>
            <div class="form-item email-link">
              <a href="#" @click.prevent="useEmail = true">Или зарегистрироваться с помощью почты</a>
            </div>
            <div class="form-item" v-if="codeSent && resendTimer > 0">
              <p>Вы сможете отправить код повторно через {{ resendTimer }} секунд.</p>
            </div>
            <div class="form-item" v-if="codeSent && resendTimer === 0">
              <button type="button" class="primary-button" @click="resendCode">Выслать код повторно</button>
            </div>
          </template>
          <template v-else>
            <div class="form-item">
              <input v-model="form.email" type="email" placeholder="Введите email" />
            </div>
            <div class="form-item">
              <input v-model="form.password" type="password" placeholder="Введите пароль" />
            </div>
            <div class="form-item">
              <input v-model="form.confirmPassword" type="password" placeholder="Повторите пароль" />
            </div>
            <div class="form-item">
              <!-- Капча, замените это на вашу реальную капчу -->
              <input type="text" placeholder="Введите капчу" />
            </div>
            <div class="form-item">
              <button type="submit" class="primary-button">Зарегистрироваться</button>
            </div>
          </template>
        </template>
        <template v-else>
          <div class="form-item">
            <input v-model="form.email" type="email" placeholder="Введите email" />
          </div>
          <div class="form-item">
            <input v-model="form.password" type="password" placeholder="Введите пароль" />
          </div>
          <div class="form-item">
            <button type="submit" class="primary-button">Войти</button>
          </div>
        </template>
        <div class="social-autorisation">
          <div class="subhead">Авторизоваться с помощью</div>
          <div class="social-buttons">
            <button class="social-button" aria-label="Facebook">
              <i class="el-icon-facebook"></i>
            </button>
            <button class="social-button" aria-label="Google">
              <i class="el-icon-google"></i>
            </button>
            <button class="social-button" aria-label="Twitter">
              <i class="el-icon-twitter"></i>
            </button>
            <button class="social-button" aria-label="Instagram">
              <i class="el-icon-instagram"></i>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const authMode = ref('Вход');
    const useEmail = ref(false);
    const codeSent = ref(false);
    const sendingCode = ref(false);
    const resendTimer = ref(0);
    const form = ref({
      phone: '',
      email: '',
      password: '',
      confirmPassword: '',
      verificationCode: ''
    });

    const errorMessage = ref('');
    const router = useRouter();

    const login = () => {
      if (form.value.email === 'user@user.ru' && form.value.password === 'user') {
        errorMessage.value = '';
        router.push('/');
        console.log('Авторизируйся сука')
      } else {
        errorMessage.value = 'Неверные логин или пароль';
      }
      console.log('Авторизируйся сука')
    };

    const sendCode = () => {
      sendingCode.value = true;
      // Логика отправки кода
      setTimeout(() => {
        sendingCode.value = false;
        codeSent.value = true;
        startResendTimer();
        console.log('Код отправлен на:', form.value.phone);
      }, 2000); // Имитация задержки для отправки кода
    };

    const verifyCode = () => {
      // Логика проверки кода
      console.log('Проверка кода:', form.value.verificationCode);
    };

    const resendCode = () => {
      if (resendTimer.value === 0) {
        sendCode();
      }
    };

    const startResendTimer = () => {
      resendTimer.value = 60;
      const timer = setInterval(() => {
        if (resendTimer.value > 0) {
          resendTimer.value--;
        } else {
          clearInterval(timer);
        }
      }, 1000);
    };

    const handleFormSubmit = () => {
      if (authMode.value === 'Регистрация') {
        if (useEmail.value) {
          // Логика регистрации через email
          console.log('Регистрируем с:', form.value.email, form.value.password);
        } else {
          verifyCode();
        }
      } else {
        login();
      }
    };

    return {
      authMode,
      useEmail,
      codeSent,
      errorMessage,
      sendingCode,
      resendTimer,
      form,
      sendCode,
      verifyCode,
      resendCode,
      handleFormSubmit,
    };
  },
};
</script>

<style scoped>
/* Стили остаются без изменений */
.error-message {
  color: red;
  font-size: 14px;
  text-align: center;
  margin-bottom: 10px;
}
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  background-image: url('@/assets/moscow_bg_map.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.auth-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 500px;
  padding: 100px;
  gap: 30px;
  height: 50vh;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.logo img {
  display: block;
  margin: 0 auto;
  height: 50px;
}

.description {
  text-align: center;
  margin: 20px 0;
  background-color: #F8F8F8;
  color: #616161;
  padding: 20px;
  border-radius: 20px 20px 20px 0;
}

.toggle {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 20px;
}

.toggle label {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.toggle input[type="radio"] {
  margin-right: 8px;
}

.auth-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.form-item {
  width: 70%;
  max-width: 400px;
  margin-bottom: 15px;
}

.form-item input {
  width: 100%;
  height: 45px;
  border-radius: 20px;
  padding: 0 15px;
  font-size: 14px;
  border: 1px solid #dcdcdc;
  box-shadow: none;
}

.form-item input:focus {
  border-color: #835DF0;
  box-shadow: 0 0 5px rgba(131, 93, 240, 0.3);
}

.primary-button {
  width: 100%;
  height: 45px;
  background-color: #835DF0;
  border: none;
  border-radius: 20px;
  color: #ffffff;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
}

.primary-button:hover {
  background-color: #6f4fb0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.email-link {
  text-align: center;
}

.social-autorisation {
  text-align: center;
  gap: 10px;
  margin-top: 20px;
}

.subhead {
  margin-bottom: 20px;
  color: #616161;
}

.social-buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.social-button {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  background-color: #e0e0e0;
  border: none;
  cursor: pointer;
}

.social-button:hover {
  background-color: #dcdcdc;
}
</style>
