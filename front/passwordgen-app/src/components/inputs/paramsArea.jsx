import styles from 'src/styles/inputs/paramsArea.module.css'

function ParamsArea(props) {
    return (
        <div className={styles.paramsArea}>
            {props.children}
        </div>
    );
}

export default ParamsArea;