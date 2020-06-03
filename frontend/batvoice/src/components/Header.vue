<template>
  <header class="header">
    <h1>batvoice</h1>
    <div v-if="isLoggedIn">
      <button class="btn" @click="logout">Logout</button>
    </div>
  </header>
</template>

<script>
export default {
  name:"Header",
  data(){
    console.log("in data");
    return{
      isLoggedIn: false
    }
  },
  mounted(){
    this.isLoggedIn= localStorage.getItem('token') ? true : false;
  },
  methods:{
    logout(){
      localStorage.removeItem('token');
      this.$router.replace('/');
      this.isLoggedIn = false;
    }
  }

}
</script>

<style lang="css" scoped>
.header {
  background: #3FBEF7;
  color:#fff;
  text-align: center;
  padding: 20px;
  display: flex;
  justify-content: space-around;
}
h1{
  display: inline-block;
}
button{
  margin-left: auto;
  display: inline-block;
  background-color: #277BBD;
  box-shadow: 1px 2px 3px 1px rgba(39,123,189, 0.5);
}
button:hover{
  background-color: #277BBD;
}
</style>
