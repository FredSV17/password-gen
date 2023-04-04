import styles from 'src/styles/generatorBody.module.css'
import PasswordParam  from './inputs/passwordParam';
import { getPassword } from 'src/services/passwordGen';
import 'react-dropdown/style.css';
import { Component } from 'react';
import GenerateButton from './generateButton';


class GeneratorBody extends Component {
    state = { partsOfSpeech: {text: "adjective", options: [  { value: "verb", label: "verb" },{ value: "adjective", label: "adjective" } ], withCheckbox: true},
              divisory: {text: "_", options: null, withCheckbox: false}, 
              symbol: {text: "@", options: null, withCheckbox: false}, 
              minNumRand: {text: "1", options: null, withCheckbox: false}, 
              maxNumRand: {text: "100", options: null, withCheckbox: false}, 
              substantive: {text: "ANIMAL", options: [ { value: 'ANIMAL', label: 'ANIMAL' },{ value: 'NOUN', label: 'NOUN' },{ value: 'PERSON', label: 'PERSON' },{ value: 'RANDOM', label: 'RANDOM' }], withCheckbox: false},
              password:"example_example@16"
            }

    sendText = () => {
        const body = {
            substantive_type: this.state.substantive.text,
            parts_of_speech: this.state.partsOfSpeech.text, 
            separator: this.state.divisory.text,
            special_character: this.state.symbol.text,
            max_num_rand: this.state.maxNumRand.text,
            min_num_rand: this.state.minNumRand.text
        }
        console.log(body)
        getPassword(body,this.setPassword)
    }

    setPassword = (password) => this.setState({password: password})
    
    setText = (text, pattern) => {
        this.setState({
            [pattern]: {text: text} 
        })
    }

    inputParams = Object.keys(this.state).map((keyName, keyIndex) => {
            if (keyName != "password"){
                return <PasswordParam key={keyIndex+keyName} setInputValue={this.setText} patternTitle={keyName} value={this.state[keyName].text} options={this.state[keyName].options} withCheckbox={this.state[keyName].withCheckbox}/> 
            }
        })

    
    render() { 
        return (
            <div className={styles.generatorBody}>
            {this.inputParams}
            <h1 className={styles.passwordArea}>{this.state.password}</h1>
            <GenerateButton clickCallback={this.sendText}><h1>Generate!</h1></GenerateButton>
        </div>
        );
    }
}
 
export default GeneratorBody;