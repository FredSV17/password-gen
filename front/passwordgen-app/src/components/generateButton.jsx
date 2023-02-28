import styles from '@/styles/generateButton.module.css'

function GenerateButton(props) {
    return ( 
        <div className={styles.buttonArea}>
            <button onClick={props.clickCallback} className={styles.generateButton}>{props.children}</button>
        </div>
     );
}

export default GenerateButton;