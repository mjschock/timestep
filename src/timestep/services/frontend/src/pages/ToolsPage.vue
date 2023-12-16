<template>
  <q-table
    :title="title"
    :rows="rows"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

const pageType = 'Tool'

export default defineComponent({
  name: `${pageType}sPage`,
  setup () {
    const columns = [
      {
        align: 'left',
        field: row => row.name,
        label: 'Name',
        name: 'name',
        sortable: true
      },
    ]
    const rows = ref([])
    const selected = ref([])
    const title = `${pageType}s`

    return {
      columns,
      rows,
      selected,
      title,
      getSelectedString () {
        return selected.value.length === 0 ? '' : `${selected.value.length} ${pageType.toLowerCase()}${selected.value.length > 1 ? 's' : ''} selected of ${rows.value.length}`
      },
    }
  }
})
</script>
