package com.project.readtimespring.Data;


import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "keydata")
public class GetData {

    @Id
    int id;
    String name;
    String keySign;
    int timeClick;
    int timeNext;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getKeySign() {
        return keySign;
    }

    public void setKeySign(String keySign) {
        this.keySign = keySign;
    }

    public int getTimeClick() {
        return timeClick;
    }

    public void setTimeClick(int timeClick) {
        this.timeClick = timeClick;
    }

    public int getTimeNext() {
        return timeNext;
    }

    public void setTimeNext(int timeNext) {
        this.timeNext = timeNext;
    }
}
