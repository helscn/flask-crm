export default function () {
  return {
    id: '',
    name: '',
    title:'',
    department:'',
    phone:'',
    email:'',
    token: localStorage.getItem('Token') ? localStorage.getItem('Token') : ''
  }
}
