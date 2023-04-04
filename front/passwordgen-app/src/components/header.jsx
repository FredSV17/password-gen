import styles from 'src/styles/header.module.css'

function Header() {
    return (  
        <div className={styles.header}>
            <h1>
                Readable password generator
            </h1>
        </div>
    );
}

export default Header;