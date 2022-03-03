import React, { Component } from 'react';
import axios from 'axios';

export default class requester extends Component {
    constructor(props) {
        super(props);

        this.state = {data: [{}]}
        this.getAllRecipes = this.getAllRecipes.bind(this);
    }

    getAllRecipes() {
        axios.get('http://127.0.0.1:5000/api/recipes')
        .then(response => {
            // handle success
            console.log(response);
        })
        .catch(error => {
            // handle error
            console.log(error);
        });
    }

  render() {

    this.getAllRecipes();

    return (
      <div>requester</div>
    )
  }
}
