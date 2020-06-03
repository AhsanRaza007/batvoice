<template>
  <div class="home">
    <router-link to="/login"><button class="btn">Login</button></router-link>
    <router-link to="/register"><button class="btn">Register</button></router-link>
  </div>
</template>

<script>
export default {
  name:"Home",
  created(){
    if(localStorage.getItem('token'))
      this.$router.push('/audio')
  }
}
</script>

<style lang="css" scoped>
  .home{
    display: inline-block;
    margin: 100px;
    display: flex;
    justify-content:center;
  }
  .home button{
    margin:50px;
  }
</style>
