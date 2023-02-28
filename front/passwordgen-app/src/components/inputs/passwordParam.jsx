import styles from '@/styles/inputs/passwordParam.module.css'
import { useState } from 'react';
import DropdownCheckbox from '../etc/dropdownCheckbox';

function PasswordParam(props) {
    const [input, setInput] = useState(props.value)
    const options = props.options

    const setText = (value, patternTitle) => { 
        setInput(value)
        props.setInputValue(value,patternTitle)
    }
    
    const setInputValues = (inputValue) => {
        let options = []
        if (!Array.isArray(inputValue))
         options = inputValue
        else
            if (inputValue.length > 1)
                options = inputValue.reduce((accumulator, currentValue) => accumulator.value + ';' + currentValue.value)
            else
                options = inputValue[0]?.value
        setText(options,props.patternTitle);
    }

    const setInputType = () => {if(props.options == null)
                                    return <input onChange={((e) => setText(e.target.value,props.patternTitle))} className={styles.inputName} value={input}></input>
                                else
                                    return <DropdownCheckbox className={styles.patternDropdown} onChange={((e) => setText(e.value,props.patternTitle))} options={options} value={input} withCheckbox={props.withCheckbox} valueChange={setInputValues}/>
    }
    return (
        <span className={styles.patternInput}>
            <h1>{props.patternTitle}</h1>
            {setInputType()}
        </span>
    );
}
export default PasswordParam;