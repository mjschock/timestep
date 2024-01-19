<template>
  <q-table
    title="Calendars"
    :rows="calendars"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'CalendarsPage',
  setup () {
    const columns = [
      {
        align: 'left',
        field: calendar => calendar.name,
        label: 'Name',
        name: 'name',
        sortable: true
      },
    ]
    const calendars = ref([])
    const selected = ref([])

    return {
      columns,
      calendars,
      selected,
      getSelectedString () {
        // return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${documents.length}`
        return selected.value.length === 0 ? '' : `${selected.value.length} calendar${selected.value.length > 1 ? 's' : ''} selected of ${accounts.value.length}`
      },
    }
  }
})
</script>
