import axios from "axios";

export default ({
    name: 'auth',
    stateFactory: true,
    namespaced: true,
    state: {
        token: null,
        user: null
    },

    getters: {
        authenticated (state) {
          return state.token
        }
    },

    mutations: {
        SET_TOKEN (state, token) {
            state.token = token
        },

        SET_USER (state, data) {
            state.data = data
        }
    },

    actions: {
        async singIn({ dispatch }, credentials) {
            try {
                let response = axios.post('http://127.0.0.1:8000/api/playbil/auth/token/login/', credentials);
                dispatch('attempt', (await response).data.auth_token)
            } catch (e) {
                alert("Невірний логін або пароль");
            }

        },

        async Register(_, credentials) {
            let response = axios.post('http://127.0.0.1:8000/api/playbil/auth/users/', credentials);
            console.log((await response).data)
        },

        async attempt ({ commit }, token) {
            commit('SET_TOKEN', token);
        },

        singOut ({ commit }) {
            return commit('SET_TOKEN', null)

        }
    }
})