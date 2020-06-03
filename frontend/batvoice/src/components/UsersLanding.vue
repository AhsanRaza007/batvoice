<template lang="html">
  <div class="container">

    <div :key="transcript.id" v-for="transcript in transcripts">


      <Transcript :transcript="transcript" :errors="errors" v-on:update="setTranscript($event)"/>
    </div>
    <h4 v-if="errorTop">{{errorTop}}</h4>
    <button class="btn new" @click="getNew">Get New Audio</button>
  </div>
</template>

<script>
import axios from 'axios';
import Transcript from './Transcript';
export default {
  name:"UserLanding",
  components:{
    Transcript,
  },
  data(){
    return{
      transcripts: [],
      errors: null,
      errorTop: null
    }
  },
  beforeCreate(){
    if(!localStorage.getItem('token'))
      this.router.replace('/login')
  },
  async created(){
    console.log("In created");
      try{
        let token = `Token ${localStorage.getItem('token')}`;
        let response = await axios.get('http://127.0.0.1:8000/api/audio/getAll',
        {headers:{
          'Authorization':token
        }});
        this.transcripts = response.data;
        console.log(response.data);
      }catch(err){
        console.log(err.response.data)
      }
  },
  methods:{
    async setTranscript(x){
      let data = {
        'id':x[0],
        'transcription':x[1],
        'audio':x[2],
        'transcribed':x[3],
        'user':x[4]
      }
      try{
        let response = await axios.put(`http://127.0.0.1:8000/api/audio/${x[0]}`, data,
        {
          headers:{
            'Authorization' : `Token ${localStorage.getItem('token')}`,
            'content-type':'application/json'
          }
        });
        // let objIndex = this.transcripts.findIndex((obj => obj.id == x[0]));
        // console.log(objIndex);
        // this.transcripts[objIndex] = response.data;
        window.location.reload();
         console.log(response.data);
      }catch(err){
        this.errors = Object.entries(err.response.data).join('\n');
      }
    },
  async getNew(){
      try{
        let response = await axios.get('http://127.0.0.1:8000/api/audio',{
            headers:{
              'Authorization' : `Token ${localStorage.getItem('token')}`,
              'content-type':'application/json'
            }
        });
        console.log(response.data);
        this.transcripts = [...this.transcripts, response.data]
      }catch(err){
        this.errorTop = err.response.data;
      }
    }
  }

}
</script>

<style lang="css" scoped>
  .errors{
    color: rgba(255, 0, 0, 0.5);
    text-align: center;
  }
  audio{
    outline: none;
    width: 100%;
  }
  input[type=text]{
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  outline: none;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button{
  width: 50%;
  padding: 10px 10px!important;
  margin: 1px auto;
  display: block;
}
.new{
  width: 100%;
  margin: 10px auto;
  display: block;
}
.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
  width: 500px;
  margin: 10px auto;
}
</style>
