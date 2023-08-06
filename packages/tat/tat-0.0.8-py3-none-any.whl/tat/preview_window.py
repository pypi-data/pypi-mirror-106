from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QLayout
from PySide6.QtGui import QImage, QResizeEvent, QPixmap, QMouseEvent
from PySide6.QtCore import QSize

from abc import abstractmethod
from typing import Optional, List

from .image_entry import ImageEntry
from .checkable_image_entry import CheckableImageEntry
from .utils import load_image, fit_to_frame


class PreviewWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget]):
        super(PreviewWindow, self).__init__(parent)
        self._selected_image_entry: Optional[ImageEntry] = None
        self._source_image_entries: List[CheckableImageEntry] = []

    @abstractmethod
    def image_preview(self) -> QLabel:
        raise NotImplementedError

    @abstractmethod
    def source_layout(self) -> QLayout:
        raise NotImplementedError

    def add_source_image_entry(self, ime: CheckableImageEntry, index: Optional[int] = None) -> None:
        self._source_image_entries.insert(len(self._source_image_entries) if index is None else index, ime)
        self.source_layout().addWidget(ime)

    def draw_preview_image(self, image: QImage) -> None:
        image_preview = self.image_preview()
        image_preview.setPixmap(
            fit_to_frame(QPixmap.fromImage(image), QSize(image_preview.width(), image_preview.height())))

    def set_preview_image(self, image: QImage, image_entry: ImageEntry) -> None:
        if image_entry is self._selected_image_entry:
            return

        self.draw_preview_image(image)
        if self._selected_image_entry is not None:
            self._selected_image_entry.setSelected(False)
        self._selected_image_entry = image_entry
        image_entry.setSelected(True)

    def clear_preview_image(self) -> None:
        self.image_preview().setText("Preview")
        if self._selected_image_entry is not None:
            self._selected_image_entry.setSelected(False)
        self._selected_image_entry = None

    def image_entry_click_handler(self, sender: ImageEntry, event: QMouseEvent) -> None:
        self.set_preview_image(load_image(sender.image_path), sender)

    def resizeEvent(self, event: QResizeEvent) -> None:
        if self._selected_image_entry is None:
            return
        self.draw_preview_image(load_image(self._selected_image_entry.image_path))

    def clear_image_entries(self) -> None:
        for ime in self._source_image_entries:
            ime.close()
        self._source_image_entries.clear()

    def select_deselect(self) -> None:
        all_checked = True
        for ime in self._source_image_entries:
            if not ime.isChecked():
                all_checked = False
                break

        for ime in self._source_image_entries:
            ime.setChecked(not all_checked)

    def get_selected_entries(self):
        selected: List[CheckableImageEntry] = []
        for ime in self._source_image_entries:
            if ime.isChecked():
                selected.append(ime)
        return selected
