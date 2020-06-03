<template>
  <div id="app">
    <Header />
    <router-view></router-view>
  </div>
</template>

<script>
import Header from './components/Header'
export default {
  name: 'App',
  components: {
    Header,
  },
  methods:{
    logout(){
      localStorage.removeItem('token');
      this.isLoggedIn= false;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
*{
  box-sizing: border-box;
  margin: 0;
}
body{
  background: #277BBD;
}
.btn{
  padding:15px 70px;
  border-radius: 10px;
  border: none;
  background-color: #3FBEF7;
  color: #fff;
  font-weight: bold;
  font-size: 20px;
  outline: none;
  box-shadow: 1px 1px 2px 3px rgba(63,190,247,0.3);
}
.btn:hover{
  cursor: pointer;
  box-shadow: none;
  background-color: rgba(63,190,247,0.9)
}
</style>
