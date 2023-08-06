class RedcapDTO:
    field_name = str()
    form_name = str()
    section_header = str()
    field_type = str()
    field_label = str()
    choices_calculations_or_slider_labels = str()
    field_note = str()
    text_validation_type_or_slider_number = str()
    text_validation_min = str()
    text_validation_max = str()
    identifier = str()
    branching_logic = str()  # Show field only if...
    required_field = bool()
    custom_alignment = str()
    question_number = str()  # surveys only
    matrix_group_name = str()
    matrix_ranking = str()
    field_annotation = str()

    def to_dict(self) -> dict:
        return vars(self)
