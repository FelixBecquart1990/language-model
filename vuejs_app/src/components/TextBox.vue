<template>
  <v-container>
    <v-row class="text-center">
      <v-col class="mx-auto mt-5" max-width="400">
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
          >Write some text then press "enter"</v-btn
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col class="mx-auto" max-width="400">
        <v-skeleton-loader
          v-if="loading"
          transition="fade-transition"
          type="list-item-two-line"
          class="mx-auto"
        ></v-skeleton-loader>
        <div class="generated-text">{{ generatedText }}</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({ text: "", generatedText: "", loading: false }),
  methods: {
    getGeneratedText() {
      this.generatedText = "";
      this.loading = true;
      let self = this;
      fetch("http://127.0.0.1:5000/", {
        method: "post",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(self.text)
      })
        .then(res => res.json())
        .then(function(data) {
          self.generatedText = data.text;
          self.loading = false;
        })
        .catch(function(err) {
          self.loading = false;
          console.log(err);
        });
    }
  }
};
</script>

<style>
.generated-text {
  color: white;
  font-size: 30px;
  margin: auto 30px;
}

.v-skeleton-loader__list-item-two-line,
.v-skeleton-loader__bone {
  background-color: transparent !important;
}
</style>
