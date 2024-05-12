<template>
  <div>
    <form @submit.prevent="submitForm">
      <label>
        URL:
        <input v-model="url" type="text" required>
      </label>
      <label>
        Format:
        <select v-model="format">
          <option value="csv">CSV</option>
          <option value="json">JSON</option>
        </select>
      </label>
      <button type="submit">Scrape</button>
    </form>
    <a v-if="downloadUrl" :href="downloadUrl" download>Download Data</a>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ScraperForm',
  data() {
    return {
      url: '',
      format: 'csv',
      downloadUrl: ''
    }
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('/scrape', { url: this.url, format: this.format }, { responseType: 'blob' })
        const blob = new Blob([response.data], { type: `text/${this.format}` })
        this.downloadUrl = window.URL.createObjectURL(blob)
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>