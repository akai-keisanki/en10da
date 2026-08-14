import axios from 'axios'
import { useRuntimeConfig } from '#app'

export const useAPI = () => {
  const { token } = useAuth()
  const config = useRuntimeConfig()

  const createAxiosInstance = () => axios.create({
      baseURL: config.public.baseURL,
      headers: {
        Authorization: `${token.value}`
      }
    })
    
  const request = async (method, url, data = null, config = {}) => {
    const ins = createAxiosInstance()

    try {
      if (method === "get" || method === "delete") {
        return await ins[method](url, config)
      } else {
        return await ins[method](url, data, config)
      }
    } catch (error) {
      console.error(error.message)
      throw error
    }
  }

  const get = (url, config = {}) => request("get", url, null, config);
  const post = (url, data, config = {}) => request("post", url, data, config);
  const put = (url, data, config = {}) => request("put", url, data, config);
  const del = (url, config = {}) => request("delete", url, null, config);

  return {get, post, put, del, request, createAxiosInstance}
}
