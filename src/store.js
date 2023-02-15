import { useMemo } from 'react'
import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import { ThunkMiddleware } from 'redux-thunk'
import reducers from './reducres'

let createStore

function initStore(initialState) {
    return createStore(
        reducers, initialState, componentWithDevTools(applyMiddleware(ThunkMiddleware))
    )
}

export const initializeStore = (preloadedState) => {
    let _store = store ?? initStore(preloadedState)

    if(preloadedState && store){
        _store = initStore({
            ...store.getState(),
            ...preloadedState,
        })
        store = undefined
    }

    if(typeof window === 'undefined') return _store
    if(!store) store = _store;

    return _store;
}

export function useStore(initialState){
    const store = useMemo(() => initializeStore(initialState), [initialState])
    return store
}