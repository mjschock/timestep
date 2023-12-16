<template>
  <!-- <q-card-section> -->
    <!-- <div class="text-h6">Documents</div> -->
    <!-- <div class="text-subtitle2">Primary</div> -->
  <!-- </q-card-section> -->

  <q-table
    title="Documents"
    :rows="documents"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />

  <!-- <div class="q-mt-md">
    Selected: {{ JSON.stringify(selected) }}
  </div> -->

  <!-- <q-card-section> -->
    <!-- <q-list>
      <q-item v-for="document in documents" :key="document.id">
        <q-item-section>
          <q-item-label>{{ document.name }}</q-item-label>
        </q-item-section>

        <q-item-section side>
          <q-btn
            color="primary"
            dense
            icon="cloud_download"
            round
          />
        </q-item-section>
      </q-item>
    </q-list> -->
  <!-- </q-card-section> -->

  <!-- <q-card-actions vertical v-if="!selected.length">
    <q-form>
      <q-card-actions vertical>
        <q-file
          :model-value="files"
          @update:model-value="updateFiles"
          label="Upload document"
          outlined
          multiple
          :clearable="!isUploading"
        >
          <template v-slot:file="{ index, file }">
            <q-chip
              class="full-width q-my-xs"
              :removable="isUploading && uploadProgress[index].percent < 1"
              square
              @remove="cancelFile(index)"
            >
              <q-linear-progress
                class="absolute-full full-height"
                :value="uploadProgress[index].percent"
                :color="uploadProgress[index].color"
                track-color="grey-2"
              />

              <q-avatar>
                <q-icon :name="uploadProgress[index].icon" />
              </q-avatar>

              <div class="ellipsis relative-position">
                {{ file.name }}
              </div>

              <q-tooltip>
                {{ file.name }}
              </q-tooltip>
            </q-chip>
          </template>

          <template v-slot:after v-if="canUpload">
            <q-btn
              color="primary"
              dense
              icon="cloud_upload"
              round
              @click="upload"
              :disable="!canUpload"
              :loading="isUploading"
            />
          </template>
        </q-file>
      </q-card-actions>
    </q-form>
  </q-card-actions> -->

  <q-card-actions vertical v-if="!selected.length">
    <q-form @submit="uploadDocument">
      <q-card-actions vertical>
        <q-file
          label="Document"
          :model-value="files"
          @update:model-value="updateFiles"
          lazy-rules
        >
          <!-- <template v-slot:append>
            <q-icon
              name="cloud_upload"
              class="cursor-pointer"
              @click="uploadDocument"
            />
          </template> -->
        </q-file>
        <q-btn
          color="primary"
          label="Upload document"
          no-caps
          type="submit"
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>

  <q-card-actions vertical v-if="selected.length">
    <q-form @submit="deleteDocument">
      <q-card-actions vertical>
        <q-input
          type="text"
          label="Document"
          v-model="selected[0].name"
          lazy-rules
        >
          <template v-slot:append>
            <q-icon
              name="cloud_download"
              class="cursor-pointer"
              @click="() => downloadDocument(selected[0].id)"
            />
            <!-- <q-icon
              name="delete"
              class="cursor-pointer"
              @click="deleteDocument"
            /> -->
          </template>
        </q-input>
        <q-btn
          color="primary"
          label="Delete document"
          no-caps
          type="submit"
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>

</template>

<script lang="ts">
import { computed, defineComponent, onBeforeUnmount, ref } from 'vue'
import { nhost } from 'src/boot/nhost';
import gql from 'graphql-tag'
import { StorageUploadFileParams, StorageUploadFormDataParams } from '@nhost/nhost-js';

export default defineComponent({
  name: 'DocumentsPage',

  setup () {
    const columns = [
      {
        align: 'left',
        field: doc => doc.name,
        label: 'Name',
        name: 'name',
        sortable: true
      },
      // {
      //   align: 'left',
      //   field: doc => doc.bucketId,
      //   label: 'Bucket',
      //   name: 'bucketId',
      //   sortable: true
      // },
      // {
      //   align: 'left',
      //   field: doc => doc.id,
      //   label: 'ID',
      //   name: 'id',
      //   sortable: true
      // },
    ]
    const documents = ref([])
    const files = ref([])
    const uploadProgress = ref([])
    const selected = ref([])
    const timeoutID = ref<Timeout | undefined>(undefined)

    async function getDocuments () {
      const FILES = gql`
        query {
          files {
            id
            bucketId,
            name
          }
        }
      `
      const { data, error } = await nhost.graphql.request(FILES)

      if (error) {
        console.error(error)
        return
      }

      documents.value = data.files
    }

    getDocuments()

    function cleanUp () {
      clearTimeout(timeoutID.value)
    }

    function updateUploadProgress () {
      let done = true

      uploadProgress.value = uploadProgress.value.map(progress => {
        if (progress.percent === 1 || progress.error === true) {
          return progress
        }

        const percent = Math.min(1, progress.percent + Math.random() / 10)
        const error = percent < 1 && Math.random() > 0.95

        if (error === false && percent < 1 && done === true) {
          done = false
        }

        return {
          ...progress,
          error,
          color: error === true ? 'red-2' : 'green-2',
          percent
        }
      })

      timeoutID.value = done === true
        ? undefined
        : setTimeout(updateUploadProgress, 300)
    }

    onBeforeUnmount(cleanUp)

    return {
      columns,
      documents,
      files,
      selected,
      uploadProgress,
      // timeoutID,
      getSelectedString () {
        // return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${documents.length}`
        return selected.value.length === 0 ? '' : `${selected.value.length} document${selected.value.length > 1 ? 's' : ''} selected of ${documents.value.length}`
      },

      isUploading: computed(() => timeoutID.value !== undefined),
      canUpload: computed(() => files.value !== null),

      cancelFile (index) {
        this.uploadProgress[ index ] = {
          ...this.uploadProgress[ index ],
          error: true,
          color: 'orange-2'
        }
      },

      async deleteDocument () {
        console.log('selected.value', selected.value)
        console.log('selected.value[0].id', selected.value[0].id)
        const user = nhost.auth.getUser()
        const storageDeleteFileParams: StorageDeleteFileParams = {
          // bucketId: user?.id,
          fileId: selected.value[0].id,
          // id: bucketId,
          // name: files.value[0].name,
          // name: 'test'
        }
        await nhost.storage.delete(storageDeleteFileParams)
      },

      async downloadDocument () {
        const user = nhost.auth.getUser()
        const storageDownloadFileParams: StorageDownloadFileParams = {
          bucketId: user?.id,
          fileId: selected.value[0].id,
          // id: bucketId,
          // name: files.value[0].name,
          // name: 'test'
        }
        await nhost.storage.download(storageDownloadFileParams)
      },

      updateFiles (newFiles) {
        console.log('newFiles', newFiles)
        files.value = newFiles
        // uploadProgress.value = (newFiles || []).map(file => ({
        //   error: false,
        //   color: 'green-2',
        //   percent: 0,
        //   icon: file.type.indexOf('video/') === 0
        //     ? 'movie'
        //     : (file.type.indexOf('image/') === 0
        //         ? 'photo'
        //         : (file.type.indexOf('audio/') === 0
        //             ? 'audiotrack'
        //             : 'insert_drive_file'
        //           )
        //       )
        // }))
      },

      async uploadDocument () {
        cleanUp()

        console.log('files.value', files.value)

        // await nhost.storage.upload({ file })

        // const fd = new FormData()

        // fd.append('file', fs.createReadStream('./tests/assets/sample.pdf'))
        // for (const file of files.value) {
        //   fd.append('file', file)
        // }

        const user = nhost.auth.getUser()
        const storageUploadFileParams: StorageUploadFileParams = {
          bucketId: user?.id,
          // file: files.value[0],
          file: files.value,
          // id: bucketId,
          // name: files.value[0].name,
          // name: 'test'
        }
        await nhost.storage.upload(storageUploadFileParams)

        // const storageUploadFormDataParams: StorageUploadFormDataParams = {
        //   bucketId: bucketId,
        //   formData: fd,
        // }
        // await nhost.storage.upload(storageUploadFormDataParams)

        // const allDone = uploadProgress.value.every(progress => progress.percent === 1)

        // uploadProgress.value = uploadProgress.value.map(progress => ({
        //   ...progress,
        //   error: false,
        //   color: 'green-2',
        //   percent: allDone === true ? 0 : progress.percent
        // }))

        // updateUploadProgress()
      },

      // async uploadDocument () {
      //   const user = nhost.auth.getUser()
      //   const storageUploadFileParams: StorageUploadFileParams = {
      //     bucketId: user?.id,
      //     file: files.value[0],
      //     // id: bucketId,
      //     // name: files.value[0].name,
      //     // name: 'test'
      //   }
      //   await nhost.storage.upload(storageUploadFileParams)
      // },
    }
  }
})
</script>
