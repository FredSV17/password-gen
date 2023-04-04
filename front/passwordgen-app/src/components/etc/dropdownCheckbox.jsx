import { useState } from "react";
import Select, { components } from "react-select";

export default function DropdownCheckbox(props) {
  const [selectedOptions, setSelectedOptions] = useState([]);

  const InputOption = ({
    getStyles,
    Icon,
    isDisabled,
    isFocused,
    isSelected,
    children,
    innerProps,
    ...rest
  }) => {
    const [isActive, setIsActive] = useState(false);
    const onMouseDown = () => setIsActive(true);
    const onMouseUp = () => setIsActive(false);
    const onMouseLeave = () => setIsActive(false);

    // styles
    let bg = "transparent";
    if (isFocused) bg = "#eee";
    if (isActive) bg = "#B2D4FF";

    const style = {
      alignItems: "center",
      backgroundColor: bg,
      color: "inherit",
      display: "flex ",
    };

    // prop assignment
    const propsInput = {
      ...innerProps,
      onMouseDown,
      onMouseUp,
      onMouseLeave,
      style,
    };
    return (
      <components.Option
        {...rest}
        isDisabled={isDisabled}
        isFocused={isFocused}
        isSelected={isSelected}
        getStyles={getStyles}
        innerProps={propsInput}
      >
        <input type="checkbox" checked={isSelected} onChange={() => {}} />
        {children}
      </components.Option>
    );
  };

  const style = {
    color: "black"
  };


  const setInputType = () => {
    if (props.withCheckbox) {
      return (
        <Select
          defaultValue={props.options[0]}
          isMulti
          closeMenuOnSelect={false}
          hideSelectedOptions={false}
          styles={style}
          onChange={(options) => {
            if (Array.isArray(options)) {
              setSelectedOptions(options.map((opt) => opt.value));
              props.valueChange(options);
            }
          }}
          options={props.options}
          components={{
            Option: InputOption,
          }}
        />
      );
    } else {
      return (
        <Select
          className="basic-single"
          classNamePrefix="select"
          defaultValue={props.options[0]}
          name="color"
          styles={style}
          onChange={(options) => {
            setSelectedOptions(options.value);
            props.valueChange(options.value);
          }}
          options={props.options}
        />
      );
    }
  };

  return (
    <div>
      {setInputType()}
    </div>
  );
}
