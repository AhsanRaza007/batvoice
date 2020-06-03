<template>

    <div class="form">
      <audio ref="audio" controls>
        <source :src="audioUrl" type="audio/mp3">
      </audio>
      <div v-if="!transcript.transcription">
        <input type="text" v-model="inputTranscript" placeholder="Enter the text">
        <h4 class="errors" v-if="errors">{{errors}}</h4>
        <button class="btn" v-on:click="$emit('update', [transcript.id, inputTranscript, transcript.audio, true, transcript.user])">submit</button>
      </div>
      <div v-else>
        <h3>Transcription : {{transcript.transcription}}</h3>
      </div>
    </div>


</template>

<script>
export default {
  name:"Transcript",
  data(){
    return{
      inputTranscript:'',
    }
  },
  props: {
    transcript: {
      type: Object,
      required: true
    },
    errors:{
      type:String,
    }
  },
  computed:{
    audioUrl: function(){
      let audiosrc = this.transcript.audio.substr(8);
      let audiourl = `http://127.0.0.1:8000/media/${audiosrc}`;
      return audiourl;
    }
  }
}
</script>

<style lang="css" scoped>
.errors{
  color: rgba(255, 0, 0, 0.5);
  text-align: center;
}
.form{
  border-bottom: 1px solid #277BBD;
  padding: 20px;
}
  h3{
    color: #277BBD;
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
</style>
