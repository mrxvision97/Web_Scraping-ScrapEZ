<template>
  <div id="app">
    <h1>Web Scraper</h1>
    <ScraperForm />
  </div>
</template>

<script>
import ScraperForm from './components/ScraperForm.vue'

export default {
  name: 'App',
  components: {
    ScraperForm
  }
}
</script>