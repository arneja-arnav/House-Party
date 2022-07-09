import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import RoomojoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

export default class App extends Component {
    constructor(props) {
        super(props);
}
    
    
    render() {
        return<div>
            <HomePage />
        </div>
    }
}

//This is for the Rendering of App.js component by index.html through the div id
const appDiv = document.getElementById("app");
render(<App />, appDiv);