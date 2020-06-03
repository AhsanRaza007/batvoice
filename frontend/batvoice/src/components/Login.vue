







<template>
  <form action="#" @submit.prevent="login">

    <h1>LOGIN INTO ACCOUNT</h1>
    <img src="../assets/avatar.png" alt="avatar">
    <input type="text" name="username" placeholder="Username" v-model="username">
    <input type="password" name="password" placeholder="Password" v-model="password">
    <h1 v-if="error" class="error">{{error}}</h1>
    <button type="submit" class="btn">Login</button>
  </form>
</template>

<script>
import axios from 'axios';
export default {
  name:"Login",
  data(){
    return{
      username:'',
      password:'',
      error:null
    }
  },
  methods:{
    async login(){
      try{
        let response = await axios.post('http://127.0.0.1:8000/users/login',{
          username:this.username,
          password:this.password
        });
        this.error=null;
        localStorage.setItem('token',response.data.token);
        console.log(localStorage);
        this.$router.push('/audio');
        }catch(err){
          this.error = 'username or password incorrect';
      }
    }
  }
}
</script>

<style lang="css" scoped>
img{
  width: 100px;
  border-radius: 50%;
  margin: 10px;
}
form {
  text-align: center;
  color: #3FBEF7;
  width:480px;
  margin: 30px auto;
  padding:50px;
  border-radius: 20px;
  background-color: #f6f6f6;
}
input[type=text], input[type=password] {
width: 100%;
padding: 12px 20px;
margin: 8px 0;
display: inline-block;
border: 1px solid #ccc;
box-sizing: border-box;
outline: none;
}
button{
margin: 10px auto;
width: 100%;
}
.error{
  font-size: 15px;
  color: rgba(255, 0, 0, 0.5);
}
</style>
