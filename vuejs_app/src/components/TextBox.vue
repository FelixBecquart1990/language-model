<template>
  <v-container>
    <v-row class="text-center">
      <v-col class="mx-auto mt-5 cols">
        <v-textarea
          v-model="text"
          row-height="2"
          solo
          label="Write some text here..."
          @keypress.enter="getGeneratedText()"
        ></v-textarea>
        <v-btn
          text
          color="primary"
          class="text-capitalize"
          @click="getGeneratedText()"
          v-if="text == '' || (generatedText == '' && !loading)"
        >Write some text then press "enter"</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="mx-auto cols">
        <v-skeleton-loader
          v-if="loading"
          transition="fade-transition"
          type="list-item-two-line"
          class="mx-auto"
        ></v-skeleton-loader>
        <div class="generated-text">{{ animatedText }}</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import sound_1 from "../assets/sound_1.mp3";
import sound_2 from "../assets/sound_2.mp3";

export default {
  name: "HelloWorld",

  data: () => ({
    text: "",
    generatedText: "",
    loading: false,
    animatedText: "",
    sound_1: new Audio(sound_1),
    sound_2: new Audio(sound_2)
  }),
  computed: {
    ...mapState(["results"])
  },
  methods: {
    textAnimation() {
      this.animatedText = "";
      var letters = this.generatedText.split("");
      let self = this;
      let index = 0;
      var interval = setInterval(function() {
        let random = Math.floor(Math.random() * 10);
        if (random == 1 || random == 2) {
          self.sound_2.play();
        } else if (random == 3 || random == 4) {
        } else {
          self.sound_1.play();
        }
        self.animatedText += letters[index];

        if (letters[index + 1] == undefined) {
          clearInterval(interval);
          return;
        }
        index++;
      }, 100);
    },
    getGeneratedText() {
      this.animatedText = "";
      this.generatedText = "";
      this.loading = true;
      let self = this;
      fetch("http://10.0.1.248:5000/", {
        method: "post",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(self.text)
      })
        .then(res => res.json())
        .then(function(data) {
          console.log(data);
          self.generatedText = data.text;
          self.textAnimation();
          self.loading = false;
        })
        .catch(function(err) {
          self.loading = false;
          console.log(err);
          self.generatedText = self.text + "...";
          self.textAnimation();
          self.$store.commit("setSnackbar", {
            color: "error",
            timeout: 3000,
            text: err
          });
        });
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Source+Code+Pro");

/* Animation */
/*p {
  animation: animated-text 4s steps(29,end) 1s 1 normal both,
             animated-cursor 600ms steps(29,end) infinite;
}

p: nth-child(2)
{
    white-space:nowrap;
    overflow:hidden;    
   animation: animated-text2 4s steps(29,end) 1s 1 normal both;
    -webkit-animation-delay: 5s; 
    animation-delay: 5s;
    -webkit-animation-fill-mode: forwards;
    animation-fill-mode: forwards;
}

/* text animation */

/*@keyframes animated-text{
  from{width: 0;}
  to{width: 472px;}
}

@keyframes animated-text2{
  from{width: 0;}
  to{width: 472px;}
}

/* cursor animations */

/*@keyframes animated-cursor{
  from{border-right-color: rgba(0,255,0,.75);}
  to{border-right-color: transparent;}
}*/

.generated-text {
  color: white;
  font-size: 30px;
  margin: auto 30px;
}

.v-skeleton-loader__list-item-two-line {
  background-color: transparent !important;
}
.cols {
  max-width: 400px !important;
}
</style>
